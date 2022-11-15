from typing import Union
from pathlib import Path
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

import random
import string

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health_check")
def health_check():
    return True

@app.get("/create_buckets")
def create_bucket():
    bucket_prefix=get_random_string(20)
    return bucket_prefix

@app.post("/start_opendata_batch")
def start_opendata_batch():
    return True

@app.get("/status")
def status():
    return True

@app.post('/upload/files')
async def upload_files(files: list[UploadFile]):
    result = []
    for file in files:
        path = Path('/tmp') / file.filename
        size = path.write_bytes(await file.read())
        result.append({'file': path, 'bytes': size})
    return result

from fastapi.responses import HTMLResponse
app = FastAPI()


@app.get('/upload/form')
async def upload_form_file():
    return HTMLResponse(content="""
        <form method="post" action="/upload/files" enctype="multipart/form-data">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>""")

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str