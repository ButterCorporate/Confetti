from PIL import Image
import pytesseract
import webbrowser
import unidecode
import pyscreenshot

def takeScreenshot(x1,y1,x2,y2):
    screenshot = pyscreenshot.grab(bbox=(x1,y1,x2,y2))  # Limita la pantalla
    screenshot.save('/Users/agusquintanar/Desktop/picture.png')

def getTextFromImage():
    imagen = Image.open('/Users/agusquintanar/Desktop/picture.png')
    text = pytesseract.image_to_string(imagen, lang="spa")
    sentence = unidecode.unidecode(text)
    search_a = sentence.replace(' ', '+')
    print(sentence)
    search_a = (search_a.split("\n\n"))
    for i in range(0, 4):
        search_a[i] = search_a[i].replace("\n", "")
    return search_a

def search():
    # Variables
    tabUrl = "http://google.com/?#q="
    # Taking the screenshot
    takeScreenshot(0, 420, 550, 800)
    # Getting the text from the image
    getTextFromImage()
    # Making an usable array
    search_a = getTextFromImage()
    q = search_a[0]  # This is the text of the question
    a1 = search_a[1]  # Text of the options
    a2 = search_a[2]
    a3 = search_a[3]

    # Searching
    command = input('Option: ')

    if command == "q":
        webbrowser.open(tabUrl + q, new=2)
    elif command == "a":
        webbrowser.open(tabUrl + a1, new=2)
        webbrowser.open(tabUrl + a2, new=2)
        webbrowser.open(tabUrl + a3, new=2)
    elif command.startswith('a'):
        webbrowser.open(tabUrl + command, new=2)
    elif command == "qa":
        webbrowser.open(tabUrl + q + a1, new=2)
        webbrowser.open(tabUrl + q + a2, new=2)
        webbrowser.open(tabUrl + q + a3, new=2)
    elif command.startswith('qa'):
        webbrowser.open(tabUrl + q + search_a[int(command[-1])], new=2)
    elif command == 'i':
        webbrowser.open(tabUrl + a1 + '+imagenes', new=2)
        webbrowser.open(tabUrl + a2 + '+imagenes', new=2)
        webbrowser.open(tabUrl + a3 + '+imagenes', new=2)
    elif command.startswith('i'):
        webbrowser.open(tabUrl + search_a[int(command[-1])] + '+imagenes', new=2)
    else:
        print('Not a valid command')

search()