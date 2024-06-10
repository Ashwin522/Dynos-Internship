from pdf2image import convert_from_path
import pytesseract
import os

def pdf_to_images(pdf_path, max_pages=None):
    images = convert_from_path(pdf_path, first_page=1, last_page=max_pages)
    return images

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

pdf_path = "/Users/ashwinnair/Downloads/femh101.pdf"
output_text_file = os.path.expanduser("~/Desktop/extracted_text.txt")
max_pages = 10  # Set the maximum number of pages to extract

images = pdf_to_images(pdf_path, max_pages)

with open(output_text_file, "w", encoding="utf-8") as f:
    for i, image in enumerate(images):
        text = extract_text_from_image(image)
        f.write(f"Text from page {i+1}:\n{text}\n\n")

print(f"Extracted text from the first {max_pages} pages written to: {output_text_file}")
