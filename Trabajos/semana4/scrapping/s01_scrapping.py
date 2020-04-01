from bs4 import BeautifulSoup
from urllib.request import urlopen

sitio = urlopen('http://www.python.org/')
contenido = BeautifulSoup(sitio.read(), 'html.parser')

#print(contenido)

#widgets = contenido.find_all('div', class_= 'blog-widget').ul

#for widget in widgets:
#    print('\n', widget, '\n')

#wid2 = contenido.find('div', class_='blog-widget')
#find hace una búsqueda en el sitio y cuando encuentra lo que pedimos, este se detiene
#print('\n', wid2, '\n')

#wid3 = contenido.find_all('div', class_= 'medium-widget')
#titulos= []

#for widget in wid3:
#    titulo = widget.find('h2')
#    titulos.append(titulo.text)
#print(titulos)

lista = contenido.find('div', class_= 'blog-widget').ul
a_titulos = []
a_enlaces = []
for elemento in lista.find_all('li'):
    ancla = elemento.find('a')
    a_titulos.append(ancla.text)
    a_enlaces.append(ancla["href"])
#print(a_titulos)
#print(a_enlaces)

noticias = list(map(lambda t,e:(t,e), a_titulos, a_enlaces))
print(noticias)