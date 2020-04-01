import csv
from datetime import datetime
import json
#Para sumar y obtener el total de Acciones y Efectivo
with open('empresa.csv') as archivo:
    lector = csv.DictReader(archivo, delimiter=',')
    now = datetime.now()
    date= now.strftime("%m/%d/%Y")
    act=0
    efct=0
    lineas = 0
    for linea in lector:
        if lineas==0:
            print('Resultados:')
        efectivo= float(linea[' EFECTIVO'])
        acciones=int(linea[' ACCIONES'])
        act=act+acciones
        efct=efct+efectivo
        lineas += 1
    print(f'Acciones Total: {act}')
    print(f'Efectivo Total: {efct}')
#Para poner los datos en el JSON
with open('empresa.csv') as archivo:
    lector = csv.DictReader(archivo, delimiter=',')
    data= {
        "fecha": f'{date}',
        "total_efectivo": f'{efct}',
        "total_acciones": f'{act}'
    }
    data['personas']= []
    for linea in lector:
        if lineas==0:
            print('Resultados:')
        efectivo= float(linea[' EFECTIVO'])
        acciones=int(linea[' ACCIONES'])
        nombre= str(linea[' PERSONA'])
        porcentaje= (efectivo*100)/efct
        data['personas'].append({
            'nombre': f'{nombre}',
            'acciones': f'{acciones}',
            'efectivo': f'{efectivo}',
            'porcentaje': f'{porcentaje} %'})

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
print(date)
