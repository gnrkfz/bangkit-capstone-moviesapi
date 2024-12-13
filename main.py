from fastapi import FastAPI, Response
from starlette.middleware.cors import CORSMiddleware
from io import StringIO
import pandas as pd
import numpy as np
import requests
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

movies_url = "https://drive.google.com/uc?export=download&id=15HB7KBBYZ3mzsftcwbSIR6V0opwi9GR_"

def read_csv():
    response = requests.get(movies_url)
    if response.status_code == 200:
        data = StringIO(response.content.decode('utf-8'))
        df = pd.read_csv(data)
        return df
    else:
        return {"message": "Failed to fetch data"}

@app.get("/")
def index():
    return Response(content="Not Found", status_code=404)

@app.get("/genres")
def get_genres():
    df = read_csv()
    genre_count = {}
    for genre_list in df['genres'].dropna():
        for genre in genre_list.split(','):
            genre = genre.strip()
            if genre:
                if genre not in genre_count:
                    genre_count[genre] = 1
                else:
                    genre_count[genre] += 1
    sorted_genres = sorted(genre_count.items())
    genre_data = [{"genre": genre, "movie_count": count} for genre, count in sorted_genres]
    return genre_data

@app.get("/random")
def get_random_movies():
    df = read_csv()
    if isinstance(df, dict) and "message" in df:
        return df
    df = df.where(pd.notnull(df), None)
    random_movies = df.sample(n=10)
    movie_list = random_movies.to_dict(orient="records")
    return movie_list

@app.get("/get_movies")
def get_movies(genre: str = "", match_type: str = ""):
    df = read_csv()
    if isinstance(df, dict) and "message" in df:
        return df
    df = df.where(pd.notnull(df), None)
    genres = [g.strip().lower() for g in genre.split(',')]
    filtered_movies = None
    if match_type == "exact":
        filtered_movies = df[df['genres'].apply(
            lambda x: all(g.strip().lower() in [genre.strip().lower() for genre in x.split(',')] for g in genres) 
            if isinstance(x, str) else False
        )]
    elif match_type == "contains":
        filtered_movies = df[df['genres'].apply(
            lambda x: any(g.strip().lower() in [genre.strip().lower() for genre in x.split(',')] for g in genres) 
            if isinstance(x, str) else False
        )]
    if filtered_movies.empty:
        return {"message": "No movies found for the selected genres"}
    movie_count = len(filtered_movies)
    if movie_count < 10:
        random_movies = filtered_movies
    else:
        random_movies = filtered_movies.sample(n=10)
    movie_list = random_movies.to_dict(orient="records")
    return movie_list


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
