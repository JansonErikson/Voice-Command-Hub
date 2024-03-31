# pdf_manager.py
from PyPDF2 import PdfReader

def open_pdf(file_path):
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(f"Content of {file_path}:")
    print(text)
