#main.py

from fastapi import FastAPI, UploadFile, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
# import filetype

from app.config import settings
from app.predict import get_candidates


app = FastAPI()
app.mount("/static", StaticFiles(directory=settings.data_dir), name="data")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": settings.app_version}

@app.post("/predict")
def predict(file: UploadFile, request: Request):
    # save to images tmp
    contents = file.file.read()
    neighbours = get_candidates(contents, settings.k)
    # get the URLs of the images
    image_urls = [f"{request.url.scheme}://{request.url.hostname}:{request.url.port}/static/{image}" for image in neighbours]
    return {"image_urls": image_urls}

    # # get the scheme, hostname, and port of the request URL
    # scheme = request.url.scheme
    # hostname = request.url.hostname
    # port = request.url.port or 80 if scheme == "http" else 443
    
    # # get the path of the request URL
    # path = request.url.path
    # # get the parent of the path
    # parent_path = Path(path).parent
    # # build the parent URL
    # parent_url = f"{scheme}://{hostname}:{port}{parent_path}"

    # return_ = {
    #     "query": "some image search",
    #     "results": [
    #         {
    #             "href": f"{parent_url}static/{neighbours[0]}",
    #             "type": f"image/{neighbours[0].split('.')[-1]}",
    #             "other_metadata_property": "some value1"
    #         },
    #         {
    #             "href": f"{parent_url}static/{neighbours[1]}",
    #             "type": f"image/{neighbours[1].split('.')[-1]}",
    #             "other_metadata_property": "some value2"
    #         },
    #         {
    #             "href": f"{parent_url}static/{neighbours[2]}",
    #             "type": f"image/{neighbours[2].split('.')[-1]}",
    #             "other_metadata_property": "some value3"
    #         }
    #     ]
    #     }
    # return return_