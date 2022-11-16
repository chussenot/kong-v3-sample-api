from typing import Union
from fastapi import FastAPI
from ddtrace import config, patch_all


config.env = "dev"      # the environment the application is in
config.service = "app"  # name of your application
config.version = "0.1"  # version of your application
patch_all()


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

