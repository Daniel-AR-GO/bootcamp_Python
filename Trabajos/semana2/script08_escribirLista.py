import csv

with open('perritos_lista.csv', mode='w') as archivo:
    escritor = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    escritor.writerow(['perrito1', 'perrito2', 'perrito3'])

familia = {
    'perrito1' : {
        'nombre' : 'Lilo',
        'color' : 'negro',
        'raza' : 'Pastor alemán',
        'pasatiempo' : 'dormir'
    },
    'perrito2' : {
        'nombre' : 'Robin',
        'color' : 'blanco con manchas negras',
        'raza' : 'Border collie',
        'pasatiempo' : 'morder'
    },
    'perrito3' : {
        'nombre' : 'Mila',
        'color' : 'miel',
        'raza' : 'Jack russel terrier',
        'pasatiempo' : 'correr'
    },
    'perrito4' : {
        'nombre' : 'Buddy',
        'color' : 'dorado',
        'raza' : 'Golden Retriever',
        'pasatiempo' : 'jugar basquetbal'
    },
}

with open('perritos_dict.csv', mode='w') as archivo:
    titulos = ['nombre', 'color', 'raza', 'pasatiempo']
    escritor = csv.DictWriter(archivo, fieldnames= titulos)
    escritor.writeheader()
    for perrito in familia.values():
        escritor.writerow(perrito)