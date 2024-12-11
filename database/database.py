from typing import List, Union

from models.movie import Movie
from models.theater import Theater
from models.user import User
from models.comment import Comment
from models.movie import Movie

from bson import ObjectId

movie_collection = Movie
theater_collection = Theater
comment_collection = Comment
user_collection = User

from typing import Union, List
from bson import ObjectId
from datetime import datetime

async def get_movie_with_comments(movie_id: ObjectId) -> Union[None, dict]:
    try:
        print(movie_id)
        pipeline = [
            {"$match": {"_id": movie_id}},
            {
                "$lookup": {
                    "from": "comments",
                    "localField": "_id",
                    "foreignField": "movie_id",
                    "as": "comments",
                }
            },
            {
                "$project": {
                    "_id" : 0,
                    "title": 1,
                    "comments": {
                        "$map": {
                            "input": "$comments",
                            "as": "comment",
                            "in": {
                                "name": "$$comment.name",
                                "email": "$$comment.email",
                                "text": "$$comment.text",
                                "date": {"$dateToString": {"format": "%Y-%m-%dT%H:%M:%SZ", "date": "$$comment.date"}}
                            },
                        }
                    },
                }
            }
        ]
        result = await movie_collection.aggregate(pipeline).to_list(length=1)
        if not result:
            return None
        return result[0]
    except Exception as e:
        raise e

async def get_movie_with_comment_count(movie_id: ObjectId) -> Union[None, dict]:
    try:
        pipeline = [
            {"$match": {"_id": movie_id}},
            {
                "$lookup": {
                    "from": "comments",
                    "localField": "_id",
                    "foreignField": "movie_id",
                    "as": "comments",
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "title": 1,
                    "commentCount": {"$size": "$comments"}
                }
            }
        ]
        result = await movie_collection.aggregate(pipeline).to_list(length=1)
        if not result:
            return None
        return result[0]
    except Exception as e:
        raise e

async def get_movie_with_comment_count_and_imdb_rating(movie_id: ObjectId) -> Union[None, dict]:
    try:
        pipeline = [
            {"$match": {"_id": movie_id}},
            {
                "$lookup": {
                    "from": "comments",
                    "localField": "_id",
                    "foreignField": "movie_id",
                    "as": "comments",
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "title": 1,
                    "imdbRating" : "$imdb.rating",
                    "commentCount": {"$size": "$comments"}
                }
            }
        ]
        result = await movie_collection.aggregate(pipeline).to_list(length=1)
        if not result:
            return None
        return result[0]
    except Exception as e:
        raise e
    
async def get_cast_count() -> Union[None, dict]:
    try:
        pipeline = [
            {
                "$unwind": "$cast"
            },
            {
                "$group": {
                    "_id": "$cast",
                    "movieCount": {"$sum": 1}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "castMember": "$_id",
                    "movieCount": 1
                }
            },
            {
                "$sort": {
                    "movieCount": -1
                }
            }
        ]
        result = await movie_collection.aggregate(pipeline).to_list(length=None)
        if not result:
            return None
        return result[0]
    except Exception as e:
        raise e

async def get_movies_before_1950_high_rating() -> Union[None, List[dict]]:
    try:
        pipeline = [
            {
                "$match": {
                    "year": {"$lt": 1950},
                    "imdb.rating": {"$gte": 7.0}
                }
            },
            {
                "$lookup": {
                    "from": "comments",
                    "localField": "_id",
                    "foreignField": "movie_id",
                    "as": "comments",
                    "pipeline": [
                        {"$limit": 2}
                    ]
                }
            },
            {
                "$project": {
                    "_id" : 0,
                    "title": 1,
                    "releaseYear": "$year",
                    "genres": 1,
                    "imdbRating": "$imdb.rating",
                    "comments": {
                        "$map": {
                            "input": "$comments",
                            "as": "comment",
                            "in": {
                                "name": "$$comment.name",
                                "text": "$$comment.text",
                            },
                        }
                    },
                }
            }
        ]
        result = await movie_collection.aggregate(pipeline).to_list(length=None)
        if not result:
            return None
        return result
    except Exception as e:
        raise e
