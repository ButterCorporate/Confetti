import pyscreenshot

screenshot=pyscreenshot.grab(bbox=(10,10,500,500)) #Limita la pantalla
screenshot.show() #Enseña la captura de pantalla, la puedes desactivar

pyscreenshot.grab_to_file('cp.png') #Guarda la captura de pantalla