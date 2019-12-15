archivo = open('s02archivo1.txt', 'w')
#Aquí estamos abreindo en archivo en modo de escritura, eso lo hacemos al poner esa letra w
archivo.writelines('Linea1')
#Con esta función estamos escribiendo contenido dentro del archivo
archivo.close()
#Es necesario que después de escribir en el archivo demos la función close
#Algo que sucede es que después de editar, y si lo volvemos a editar para añadir, este no lo agregará
#Si no que cambiará su contenido
lineas = ['Linea1', '\n', 'Linea2 Linea2', '\n','Linea3 Linea3 Linea3', '\n', 'Linea4 Linea4 Linea4 Linea4']
archivo = open('s02archivo1.txt', 'w')
archivo.writelines(lineas)
archivo.close()
archivo = open('s02archivo1.txt', 'r')
#Ahora tenemos la r para poder estar en modo lectura
for linea in archivo:
    print(linea, end='')
#Vamos a copiar el contenido a un nuevo archivo uwu
with open('s02archivo1.txt', 'r') as entrada, open('s02archivo2.txt', 'w') as salida:
    for linea in entrada:
        salida.write(linea)