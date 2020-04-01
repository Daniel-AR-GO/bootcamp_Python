from datetime import datetime, timedelta

def de_timestamp_a_semanas(fechaIn, fechTer):
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    
    dt_inicio = datetime.fromtimestamp(fechaIn)
    dt_final = datetime.fromtimestamp(fechTer)
    
    diaI = dias_semana[dt_inicio.weekday()]
    diaF = dias_semana[dt_final.weekday()]
    
    strfI = f'\n{dt_inicio.strftime("%a")} {dt_inicio.strftime("%d")} de {dt_inicio.strftime("%b")} de {dt_inicio.strftime("%Y")}'
    strfF = f'{dt_final.strftime("%a")} {dt_final.strftime("%d")} de {dt_final.strftime("%b")} de {dt_final.strftime("%Y")}'
    
    print(strfI)
    print(strfF)
    
    tiempo = int((dt_final-dt_inicio).days /7)
    return f'Entre el {diaI} {dt_inicio.strftime("%d")} de {dt_inicio.strftime("%b")} de {dt_inicio.strftime("%Y")} y {diaF} {dt_inicio.strftime("%d")} de {dt_inicio.strftime("%b")} de {dt_inicio.strftime("%Y")} hay {tiempo}'

print(de_timestamp_a_semanas(1576454400, 1578268800))
print(de_timestamp_a_semanas(1545091200, 1577750400))

#Mon 16 de Dec de 2019
#Entre el Lunes 16 de Dec de 2019 y Lunes 6 de Jan de 2020 hay 3 semanas