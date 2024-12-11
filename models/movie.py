from pydantic import BaseModel, Field
from typing import List, Optional
from beanie import Document


class Awards(BaseModel):
    wins: Optional[int]
    nominations: Optional[int]
    text: Optional[str]


class IMDB(BaseModel):
    rating: Optional[float]
    votes: Optional[int]
    id: Optional[int]


class TomatoesViewer(BaseModel):
    rating: Optional[float]
    numReviews: Optional[int]
    meter: Optional[int]


class Tomatoes(BaseModel):
    viewer: Optional[TomatoesViewer]
    lastUpdated: Optional[str]


class Movie(Document):
    title: str
    year: int
    genres: List[str]
    cast: List[str]
    runtime: Optional[int]
    plot: Optional[str]
    fullplot: Optional[str]
    languages: Optional[List[str]]
    released: Optional[str]
    directors: Optional[List[str]]
    writers: Optional[List[str]]
    awards: Optional[Awards]
    imdb: Optional[IMDB]
    countries: Optional[List[str]]
    type: Optional[str]
    poster: Optional[str]
    tomatoes: Optional[Tomatoes]
    lastupdated: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Inception",
                "year": 2010,
                "genres": ["Action", "Sci-Fi"],
                "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
                "runtime": 148,
                "plot": "A thief who enters the dreams of others to steal secrets.",
                "fullplot": "A skilled thief leads a team on a heist into the dreams of others.",
                "languages": ["English"],
                "released": "2010-07-16T00:00:00Z",
                "directors": ["Christopher Nolan"],
                "writers": ["Christopher Nolan"],
                "awards": {"wins": 4, "nominations": 8, "text": "4 wins and 8 nominations."},
                "imdb": {"rating": 8.8, "votes": 2000000, "id": 1375666},
                "countries": ["USA", "UK"],
                "type": "movie",
                "poster": "https://example.com/poster.jpg",
                "tomatoes": {
                    "viewer": {"rating": 4.5, "numReviews": 300, "meter": 92},
                    "lastUpdated": "2024-12-10T00:00:00Z",
                },
                "lastupdated": "2024-12-10T00:00:00Z",
            }
        }

    class Settings:
        name = "movies"
