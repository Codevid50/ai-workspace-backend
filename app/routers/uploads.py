from fastapi import APIRouter, UploadFile, File
from uuid import uuid4
import shutil

router = APIRouter()

@router.post('/upload', tags=['Uploads'])
def upload_file(file: UploadFile = File(...)):
    unique_filename = f'{uuid4()}_{file.filename}'

    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "filename": unique_filename
    }