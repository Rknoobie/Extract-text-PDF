import os
import re
import shutil
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    print(f"Extracting text from: {pdf_path}")
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_billing_address(text):
    print("Extracting billing address...")
    match = re.search(r"Bill To[:\s]*(.*?)(?=\n\n|\n\s*\n|$)", text, re.IGNORECASE | re.DOTALL)
    if match:
        address = match.group(1).strip()
        # Extract only the first few lines to avoid including the entire invoice
        address_lines = address.split('\n')
        return ' '.join(address_lines[:3])  # Adjust the number of lines as needed
    return "Not found"

def sanitize_folder_name(name):
    print(f"Sanitizing folder name: {name}")
    # Replace invalid characters and limit the length of the folder name
    sanitized_name = re.sub(r'[<>:"/\\|?*\n]', '_', name)
    return sanitized_name[:100]  # Limit to 100 characters to avoid overly long names

def process_pdfs(directory):
    print(f"Processing PDFs in directory: {directory}")
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return
    
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(pdf_path)
            billing_address = extract_billing_address(text)
            print(f"Billing Address in {filename}:\n{billing_address}\n")
            
            if billing_address != "Not found":
                sanitized_address = sanitize_folder_name(billing_address)
                address_folder = os.path.join(directory, sanitized_address)
                
                if not os.path.exists(address_folder):
                    os.makedirs(address_folder)
                
                shutil.move(pdf_path, os.path.join(address_folder, filename))

# Set the directory containing the PDF files
pdf_directory = r"C:\Users\Sebastan\OneDrive\Desktop\New folder"  # Replace with your actual path

# Process the PDFs in the directory
process_pdfs(pdf_directory)
