import Myocr
import os
from pdf2image import convert_from_path # type: ignore
PDF_PATH="./test.pdf"


def pdfocr(pdf_path=PDF_PATH):
    del_list = os.listdir("./pngs")
    for f in del_list:
        file_path = os.path.join("./pngs", f)
        if os.path.isfile(file_path):
            os.remove(file_path)

    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image.save(f'./pngs/{i + 1:04d}.jpg', 'JPEG')


    del_list = os.listdir("./pngs")
    del_list.sort()
    for f in del_list:
        file_path = os.path.join("./pngs", f)
        if os.path.isfile(file_path):
            Myocr.ocr(file_path)


if __name__=="__main__":
    pdfocr()
# Myocr.ocr()