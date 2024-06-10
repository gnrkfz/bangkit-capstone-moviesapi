from fastapi import FastAPI, Response
from io import StringIO
import pandas as pd
import numpy as np
import requests
import random

app = FastAPI()

movies_url = "https://storage.googleapis.com/c241ps516-moviesdataset/movies.csv"

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
    genres = set()
    for genre_list in df['genres'].dropna():
        for genre in genre_list.split(','):
            genres.add(genre.strip())
    return sorted(list(genres))

@app.get("/random")
def get_random_movies():
    df = read_csv()
    df = df.replace({np.nan: None})
    num_movies = min(10, len(df))
    random_movies = random.sample(df.to_dict(orient='records'), num_movies)
    recommendation_movies = []
    for movie in random_movies:
        formatted_genre = ", ".join(genre.strip() for genre in movie['genres'].split(',') if genre.strip())
        formatted_movie = {
            "title": f"{movie['title']} ({movie['year']})",
            "genre": formatted_genre
        }
        recommendation_movies.append(formatted_movie)
    return recommendation_movies

@app.get("/angry")
def get_angry_movies():
    df = read_csv()
    df = df.replace({np.nan: None})
    filtered_df = df[df['genres'].str.contains('Comedy|Drama|Music|Family|Adventure|Fantasy|Animation|Science Fiction', na=False)]
    num_movies = min(10, len(filtered_df))
    random_movies = random.sample(filtered_df.to_dict(orient='records'), num_movies)
    recommendation_movies = []
    for movie in random_movies:
        formatted_genre = ", ".join(genre.strip() for genre in movie['genres'].split(',') if genre.strip())
        formatted_movie = {
            "title": f"{movie['title']} ({movie['year']})",
            "genre": formatted_genre
        }
        recommendation_movies.append(formatted_movie)
    return recommendation_movies

@app.get("/sad")
def get_sad_movies():
    df = read_csv()
    df = df.replace({np.nan: None})
    filtered_df = df[df['genres'].str.contains('Comedy|Family|Romance|Animation|Music|Adventure|Fantasy|Drama', na=False)]
    num_movies = min(10, len(filtered_df))
    random_movies = random.sample(filtered_df.to_dict(orient='records'), num_movies)
    recommendation_movies = []
    for movie in random_movies:
        formatted_genre = ", ".join(genre.strip() for genre in movie['genres'].split(',') if genre.strip())
        formatted_movie = {
            "title": f"{movie['title']} ({movie['year']})",
            "genre": formatted_genre
        }
        recommendation_movies.append(formatted_movie)
    return recommendation_movies

@app.get("/happy")
def get_happy_movies():
    df = read_csv()
    df = df.replace({np.nan: None})
    filtered_df = df[df['genres'].str.contains('Adventure|Animation|Music|Comedy|Family|Fantasy|Romance|Science Fiction', na=False)]
    num_movies = min(10, len(filtered_df))
    random_movies = random.sample(filtered_df.to_dict(orient='records'), num_movies)
    recommendation_movies = []
    for movie in random_movies:
        formatted_genre = ", ".join(genre.strip() for genre in movie['genres'].split(',') if genre.strip())
        formatted_movie = {
            "title": f"{movie['title']} ({movie['year']})",
            "genre": formatted_genre
        }
        recommendation_movies.append(formatted_movie)
    return recommendation_movies

@app.get("/disgust")
def get_disgust_movies():
    df = read_csv()
    df = df.replace({np.nan: None})
    filtered_df = df[df['genres'].str.contains('Comedy|Adventure|Fantasy|Animation|Music|Science Fiction|Family|Mystery', na=False)]
    num_movies = min(10, len(filtered_df))
    random_movies = random.sample(filtered_df.to_dict(orient='records'), num_movies)
    recommendation_movies = []
    for movie in random_movies:
        formatted_genre = ", ".join(genre.strip() for genre in movie['genres'].split(',') if genre.strip())
        formatted_movie = {
            "title": f"{movie['title']} ({movie['year']})",
            "genre": formatted_genre
        }
        recommendation_movies.append(formatted_movie)
    return recommendation_movies

@app.get("/fear")
def get_fear_movies():
    df = read_csv()
    df = df.replace({np.nan: None})
    filtered_df = df[df['genres'].str.contains('Family|Comedy|Animation|Drama|Fantasy|Adventure|Romance|Music', na=False)]
    num_movies = min(10, len(filtered_df))
    random_movies = random.sample(filtered_df.to_dict(orient='records'), num_movies)
    recommendation_movies = []
    for movie in random_movies:
        formatted_genre = ", ".join(genre.strip() for genre in movie['genres'].split(',') if genre.strip())
        formatted_movie = {
            "title": f"{movie['title']} ({movie['year']})",
            "genre": formatted_genre
        }
        recommendation_movies.append(formatted_movie)
    return recommendation_movies

@app.get("/neutral")
def get_neutral_movies():
    df = read_csv()
    filtered_df = df[df['genres'].str.contains('Documentary|Drama|History|Science Fiction|Mystery|Adventure|TV Movie|War', na=False)]
    num_movies = min(10, len(filtered_df))
    random_movies = random.sample(filtered_df.to_dict(orient='records'), num_movies)
    recommendation_movies = []
    for movie in random_movies:
        formatted_genre = ", ".join(genre.strip() for genre in movie['genres'].split(',') if genre.strip())
        formatted_movie = {
            "title": f"{movie['title']} ({movie['year']})",
            "genre": formatted_genre
        }
        recommendation_movies.append(formatted_movie)
    return recommendation_movies

@app.get("/surprise")
def get_surprise_movies():
    df = read_csv()
    df = df.replace({np.nan: None})
    filtered_df = df[df['genres'].str.contains('Mystery|Thriller|Science Fiction|Adventure|Fantasy|Action|Drama|Horror', na=False)]
    num_movies = min(10, len(filtered_df))
    random_movies = random.sample(filtered_df.to_dict(orient='records'), num_movies)
    recommendation_movies = []
    for movie in random_movies:
        formatted_genre = ", ".join(genre.strip() for genre in movie['genres'].split(',') if genre.strip())
        formatted_movie = {
            "title": f"{movie['title']} ({movie['year']})",
            "genre": formatted_genre
        }
        recommendation_movies.append(formatted_movie)
    return recommendation_movies

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)