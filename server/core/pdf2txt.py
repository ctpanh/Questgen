# import fitz

# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     text = ""
#     for page_num in range(doc.page_count):
#         page = doc.load_page(page_num).get_text()
#         print('-----------------------------')
#         print(page)
#         text += page
#     doc.close()
#     return text

# pdf_file_path = "/mnt/banana/k66/thuy/Questgen/server/core/sach-khoa-hoc-lop-4-pdf-3.pdf"
# extracted_text = extract_text_from_pdf(pdf_file_path)

# with open("output.txt", "w", encoding="utf-8") as output_file:
#     output_file.write(extracted_text)

from pdf2image import convert_from_path
import pytesseract

def extract_text_from_scanned_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    extracted_text = ""
    for image in images:
        text = pytesseract.image_to_string(image, lang='eng')  # Use the appropriate language code
        extracted_text += text + "\n"
    return extracted_text

pdf_file_path = "/mnt/banana/k66/thuy/Questgen/server/core/sach-khoa-hoc-lop-4-pdf-3.pdf"
extracted_text = extract_text_from_scanned_pdf(pdf_file_path)

with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(extracted_text)