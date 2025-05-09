from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_methods=["*"],
allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is working"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename}