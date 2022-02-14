# Verifica cambios en un sitio

import urllib2

site1 = urllib2.urlopen('https://www.ejemplo.com/')
site2 = urllib2.urlopen('https://www.ejemplo.com/')

contenido1 = site1.read()
contenido2 = site2.read()

if (contenido1 == contenido2):
    print("Sitio sin cambios")
else:
    print('El sitio fue actualizado')