from fastapi import FastAPI, HTTPException
import os
import json

app = FastAPI()


@app.get("/")
def read_data():
    return {"Hello": "World"}
