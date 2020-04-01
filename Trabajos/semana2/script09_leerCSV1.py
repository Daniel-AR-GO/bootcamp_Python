import csv

with open('perritos_dict.csv') as archivo:
    lector = csv.reader(archivo, delimiter=',')
    
    lineas = 0
    for linea in lector:
        if lineas ==0:
            print('Titulos: ', ', '.join(linea))
            lineas += 1
        else:
            print('\nNombre: ', linea[0], '\n\tColor: ', linea[1], '\n\tRaza: ', linea[2], '\n\tPasatiempo: ', linea[3] )