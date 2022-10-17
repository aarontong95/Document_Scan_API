from fastapi import FastAPI, File, UploadFile
from document_scan import scan

app = FastAPI()
@app.post("/scan")
def create_upload_file(file: UploadFile = File(...)):
    return scan(file.file)
