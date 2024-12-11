from fastapi import APIRouter, Body, Query
from fastapi.responses import JSONResponse

from beanie import PydanticObjectId

from database.database import *


router = APIRouter()

@router.get("/{id}")
async def get_movies(id: PydanticObjectId):
    try:
        movies_with_comments = await get_movie_with_comments(id)
        if not movies_with_comments:
            return {"message": "No movie found with the given ID"}

        return JSONResponse(content=movies_with_comments, status_code=200)
    except Exception as e:
        return {"error": str(e)}

@router.get("/count/{id}")
async def get_movies_with_count(id: PydanticObjectId):
    try:
        movies_with_comments = await get_movie_with_comment_count(id)
        if not movies_with_comments:
            return {"message": "No movie found with the given ID"}

        return JSONResponse(content=movies_with_comments, status_code=200)
    except Exception as e:
        return {"error": str(e)}

@router.get("/count/imdb/{id}")
async def get_movies_with_count_imdb(id: PydanticObjectId):
    try:
        movies_with_comments = await get_movie_with_comment_count_and_imdb_rating(id)
        if not movies_with_comments:
            return {"message": "No movie found with the given ID"}

        return JSONResponse(content=movies_with_comments, status_code=200)
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/cast/show")
async def get_cast():
    try:
        movies_with_comments = await get_cast_count()
        if not movies_with_comments:
            return {"message": "No movie found"}

        return JSONResponse(content=movies_with_comments, status_code=200)
    except Exception as e:
        return {"error": str(e)}

@router.get("/special/show")
async def get_cast():
    try:
        movies_with_comments = await get_movies_before_1950_high_rating()
        if not movies_with_comments:
            return {"message": "No movie found"}

        return JSONResponse(content=movies_with_comments, status_code=200)
    except Exception as e:
        return {"error": str(e)}
