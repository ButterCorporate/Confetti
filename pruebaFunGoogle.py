import webbrowser 
tabUrl = "http://google.com/?#q="
term = input('Ingresar palabra/oracion/pregunta a buscar: ')
term2 = term.replace(' ','+')
webbrowser.open(tabUrl+term2,new=2)
