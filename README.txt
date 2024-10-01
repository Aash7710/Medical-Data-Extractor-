
Medical Document Extractor

Overview
--------
This project is a Medical Document Extractor that automates the extraction of key data from medical documents, such as prescriptions and patient details. It uses Tesseract OCR and Poppler for PDF processing, and is built with FastAPI for the backend, allowing easy integration with any frontend for uploading and extracting data.

Features
--------
- PDF to Text Conversion: Extract text from medical PDFs using Tesseract OCR.
- Data Extraction: Extract relevant data fields such as patient name, medical conditions, prescription details, and more.
- File Upload: Support for uploading medical documents through a web interface or API endpoint.
- CORS Enabled: Allows communication between frontend and backend through Cross-Origin Resource Sharing.

Tech Stack
----------
- Python: Core language for the backend.
- FastAPI: For building the API endpoints.
- Tesseract OCR: For optical character recognition and text extraction.
- Poppler: To convert PDF pages into images for further processing.
- HTML/CSS & JavaScript: Simple frontend for file uploads and results display.

How to Run
----------

Prerequisites
-------------
- Python 3.x
- Install dependencies: pip install -r requirements.txt
- Poppler and Tesseract-OCR should be installed. Make sure the paths to poppler and tesseract are correctly set in the code.

Installation
------------
1. Clone the repository:
   git clone https://github.com/yourusername/medical-doc-extractor.git
2. Install the dependencies:
   pip install -r requirements.txt

Running the Application
-----------------------
1. Start the FastAPI backend:
   uvicorn main:app --reload
2. Open the frontend (index.html) in your browser and use the interface to upload a PDF for extraction.

Usage
-----
- Visit the API endpoint at http://127.0.0.1:8000/
- Use the /extract_from_doc endpoint to upload and extract information from documents. 
- Supported file formats:
  - prescription
  - patient_details

Example
-------
1. Upload a prescription PDF.
2. The system will extract patient details, medicines prescribed, directions, and more.
3. Results are displayed directly on the webpage.

Future Improvements
-------------------
- Add support for more medical document types.
- Enhance the frontend with more styling and features.

License
-------
This project is licensed under the MIT License.
