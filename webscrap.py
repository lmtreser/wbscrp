# Web Scraper con Python
# Viernes 11 de febrero de 2022

import requests
from bs4 import BeautifulSoup
import webbrowser

# URL a scrapear
url = 'http://www.ejemplo.com/'
page = requests.get(url)
print(page)

# Hacer una sopa de datos
soup = BeautifulSoup(page.content, 'html.parser')

#Pide la cantidad de filas ( 1 noticia = 2 filas)
cantidadfilas = input("Ingrese Cantidad de Noticias que desea: ")
qfilas=int(cantidadfilas)

try:
    contenedor = soup.find('table', width="80%")
    tabla = contenedor.find_all('table', width="100%")
    rows = contenedor.find_all("tr")
    texto=""
    for i in range (1,qfilas+2,2):
        texto = texto + str(rows[i+1])
except IndexError:
    print("No se encontraron tantas Noticias. Intente con otra cantidad")
except AttributeError:
    print("No se encuentra el contenido dentro del documento")
else:
    # Guardar los resultados en un archivo HTML
    f = open('index.html', 'w')
    string = """<!DOCTYPE html><html lang="en"><head>
                <meta http-equiv="content-type" content="text/html; charset=UTF-8">
                <meta charset="utf-8"><title>WEB SCRAPER</title><body>
                <h2>""" + url + "</h2>" +  texto +"</body></html>"
    f.write(string)
    f.close()

    # Abrir el navegador al terminar la operacion
    print("Abriendo archivo...")
    nombreArchivo = 'index.html'
    webbrowser.open_new_tab(nombreArchivo)
