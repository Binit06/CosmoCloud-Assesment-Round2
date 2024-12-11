# FastAPI-MongoDB-CosmoCloud

This is a FastAPI application that uses MongoDB as the database and is deployed on Render.

## API Endpoints

### 1. Get The Movie Title and Comments

- **Endpoint:** `/movies/{id}`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "title": "string",
        "comments": [
            {
                "name" : "string",
                "email" : "string",
                "text" : "string",
                "date" : "string"
            }
        ]
    }
    ```

### 2. Get movie title and the number of comments

- **Endpoint:** `/movies/count/{id}`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "title" : "string",
        "commentCount" : "integer"
    }
    ```

### 3. Get IMDB Count along with total number of comments and movie title

- **Endpoint:** `/movies/count/imdb/{id}`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "title" : "string",
        "imdbRating" : "double",
        "commentCount" : "integer"
    }
    ```

### 4. List all unique cast members

- **Endpoint:** `/movies/cast/show`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "castMember" : "string",
        "movieCount" : "integer"
    }
    ```

### 5. List all movies released before 1950 with an IMDB rating of 7.0 or higher

- **Endpoint:** `/movies/special/show`
- **Method:** `GET`
- **Request Body:**
    ```json
    {
        "title" : "string",
        "releaseYear" : "integer",
        "genres" : ["string"],
        "imdbRating" : "double",
        "comments" : [
            {
                "name" : "string",
                "text" : "string"
            }
        ]
    }
    ```
- **Response:**
    ```json
    {}
    ```

## Setup and Installation

1. Clone the repository:
     ```sh
     git clone https://github.com/Binit06/CosmoCloud-Assignment---FastAPI-MongoDB-Python.git
     ```
2. Install the dependencies:
     ```sh
     pip install -r requirements.txt
     ```
3. Run the application:
     ```sh
     uvicorn app:app --host 0.0.0.0 --port 8000
     ```

## Base URL - 
```
https://cosmocloud-assignment-fastapi-mongodb.onrender.com/
```