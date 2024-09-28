from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract
import uuid
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend's URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Medical Document Extractor API. Use the '/extract_from_doc' endpoint for extraction."}

@app.post("/extract_from_doc")
async def extract_from_doc(
    file_format: str = Form(...),
    file: UploadFile = File(...)
):
    # (Same implementation as before)

    contents = await file.read()

    # Create an uploads folder if it doesn't exist
    upload_dir = "./uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Save the uploaded file temporarily
    file_path = os.path.join(upload_dir, f"{uuid.uuid4()}.pdf")

    with open(file_path, "wb") as f:
        f.write(contents)

    try:
        # Call the extract function to process the file
        data = extract(file_path, file_format)
    except Exception as e:
        data = {'error': str(e)}

    # Remove the temporary file after processing
    if os.path.exists(file_path):
        os.remove(file_path)

    return data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
