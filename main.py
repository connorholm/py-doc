from py_doc import OCR, Document
import cv2

# general testing, see documentation for actual usage
image = cv2.imread('tests/documents/test.jpg')
ocr = OCR(image)
print(ocr.get_text())

document = Document('tests/documents/test.jpg')
print(document.get_text())
bboxes = document.get_bboxes()
print(document.get_text_from_bbox(bboxes[0]))