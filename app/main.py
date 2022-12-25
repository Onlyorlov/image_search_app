from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from app.config import settings
from app.predict import get_candidates

app = FastAPI()


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": settings.app_version}


@app.post("/predict")
def predict(file: UploadFile):
    contents = file.file.read()
    neighbours = get_candidates(contents, settings.k)
    return {"neighbours": neighbours}