from PIL import Image
import pytesseract


for i in range(1,13):
    img = Image.open("prueba"+str(i)+".jpg")
    text = pytesseract.image_to_string(img, lang = 'spa')

    print(text)
    print('-------------------------------------------------------------------------\n')

