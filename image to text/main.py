import pytesseract as py
from cv2 import imread
from termcolor import cprint

py.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

value = imread('sample.jpg')
text = py.image_to_string(value)
cprint('The extracted text is:', 'yellow')
cprint(text, 'yellow')
