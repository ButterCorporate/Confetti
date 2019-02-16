from PIL import Image
import pytesseract


for i in range(1,6):
    img = Image.open("prueba"+str(i)+".png")
    text = pytesseract.image_to_string(img)

    print(text)
    print('-------------------------------------------------------------------------\n')