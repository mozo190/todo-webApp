from PIL import Image
from pytesseract import pytesseract
from pytesseract import image_to_string


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(Image.open('image.png'))
print(text)
print(pytesseract.get_languages(config=''))


