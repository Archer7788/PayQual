from fastapi import APIRouter, UploadFile, File
import pandas as pd
import os

router = APIRouter()

UPLOAD_FOLDER = "app/uploads"

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    # Read dataset
    if file.filename.endswith(".csv"):
        df = pd.read_csv(file_path)

    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(file_path)

    else:
        return {
            "error": "Unsupported file format"
        }

    # Dataset summary
    return {
        "filename": file.filename,
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": list(df.columns),
        "missing_values": df.isnull().sum().to_dict()
    }