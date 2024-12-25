import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

def save_invoice_text(invoice_text, invoice_filename):
    """Save the extracted invoice text to a file in the current directory."""
    script_directory = os.path.dirname(os.path.realpath(__file__))  # Get the current script's directory
    invoice_path = os.path.join(script_directory, invoice_filename)  # Save in the same directory
    with open(invoice_path, "w") as file:
        file.write(invoice_text)

def main():
    pdf_path = "./sample invoice 2.pdf"  # Your input PDF file path
    invoice_filename = "invoice_extracted.txt"  # The name of the output text file
    
    # Extract text from the PDF
    raw_text = extract_text_from_pdf(pdf_path)
    
    # Save the extracted text to a file in the same directory
    save_invoice_text(raw_text, invoice_filename)
    print(f"Invoice saved to {invoice_filename}")

if __name__ == "__main__":
    main()
