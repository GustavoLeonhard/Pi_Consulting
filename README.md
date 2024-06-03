## Star Wars
Star Wars FastAPI application.

**Installation**

You can choose one of the following installation methods:

**Docker**

1. Build the Docker image:

   ```bash
   docker build -t starwars .
Run the container, exposing port 8000 for the application:

Bash
docker run -p 8000:8000 starwars


Install dependencies:

Bash
pip install -r requirements.txt

Navigate to the project's root directory (star_wars).
Run the application:

Bash
uvicorn main:app --reload

Running the Application

Once you've installed and run the application, you can access it at:

Swagger Documentation

View the swagger API documentation at http://127.0.0.1:8000/docs (or http://localhost:8000/docs if using Docker).

