import cv2
import pytesseract

imagem = cv2.imread("print_magalu.JPG")
# imread é o método do opencv que permite ler uma imagem.

caminho = r"C:\Users\Leandro\AppData\Local\Programs\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)