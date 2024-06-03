## Star Wars

This project provides a Star Wars-themed FastAPI application.

**Installation**

Choose one of the following installation methods:

**Docker**

1. Build the Docker image:

   ```bash
   docker build -t starwars .

2. Run the container, exposing port 8000 for the application:

   ```bash
   docker run -p 8000:8000 starwars

**Local Environment**

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

2. Navigate to the project's root directory

3. Run the application:

   ```bash
   uvicorn main:app --reload

**Swagger Documentation**

View the interactive API documentation at http://127.0.0.1:8000/docs (or http://localhost:8000/docs if using Docker).

**Testing with Postman**
You can run all postman test cases in this link:
https://www.postman.com/gustavo-starwars/workspace/starwars/collection/15918898-1fe09542-f122-4759-b403-80bc416eb8fb?action=share&creator=15918898
