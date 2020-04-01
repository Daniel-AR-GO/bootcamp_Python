import csv

with open('perritos_dict.csv') as archivo:
    lector = csv.DictReader(archivo, delimiter=',')
    
    lineas = 0
    for linea in lector:
        if lineas==0:
            print('Titulos: ', '_ '.join(linea))
        
        print('\nNombre: ', linea['nombre'], '\n\tColor: ', linea['color'], '\n\tRaza: ', linea['raza'], '\n\tPasatiempo: ', linea['pasatiempo'])
        lineas += 1
    print(lineas)