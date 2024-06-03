from fastapi import FastAPI
import models
from database import engine
from routers import character
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(character.router)