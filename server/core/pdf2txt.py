import os
import easyocr

from pdf2image import convert_from_path
import numpy as np


class Reader:
    def __init__(self, is_cuda=False):
        self.reader = easyocr.Reader(
            ["vi"],
            gpu=is_cuda,
            model_storage_directory=os.path.join("models"),
            download_enabled=True,
        )

    def __call__(self, img):
        return self.extract_text(img)

    def extract_text(self, img, show_text=False, show_confidence=False):
        result = self.reader.readtext(img)

        extracted_text = []

        for text in filter(lambda x: x[-1] > 0.45, result):
            box, acc_text, confidence = text
            extracted_text.append(acc_text)

        return extracted_text


def convert_pdf(pdf_path, is_cuda=False):
    reader = Reader(is_cuda)
    images = convert_from_path(pdf_path)
    full_text = ""
    for img in images:
        page = ""
        img = np.array(img)
        text = reader(img)
        for t in text:
            page += t
            page += " "
        full_text += page

        print(page)
        print("----------------")
    with open("text.txt", "w", encoding="utf-8") as file:
        file.write(full_text)
    return full_text
