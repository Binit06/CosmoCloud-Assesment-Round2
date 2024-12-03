# FastAPI-MongoDB-CosmoCloud

This is a FastAPI application that uses MongoDB as the database and is deployed on Render.

## API Endpoints

### 1. Add a New Student

- **Endpoint:** `/students/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "name": "string",
        "age": "int",
        "address": {
            "city" : "string",
            "country" : "string"
        }
    }
    ```
- **Response:**
    ```json
    {
        "id": "string"
    }
    ```

### 2. Get all Students

- **Endpoint:** `/students/`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "data" : [
            {
                "name" : "string",
                "age" : "int"
            }
        ]
    }
    ```

### 3. Get a student by ID

- **Endpoint:** `/students/{id}`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "name": "string",
        "age": "int",
        "address" : {
            "city" : "string",
            "country" : "string",
        }
    }
    ```

### 4. Delete a speceific student

- **Endpoint:** `/students/{id}`
- **Method:** `DELETE`
- **Response:**
    ```json
    {}
    ```

### 5. Update the data of a speceific student

- **Endpoint:** `/students/{id}`
- **Method:** `PATCH`
- **Request Body:**
    ```json
    {
        "name": "string",
        "age": "int",
        "address": {
            "city" : "string",
            "country" : "string"
        }
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