import datetime
inicio = datetime.datetime.now() #Obtenemos el día y hora actuales
print(inicio)
print(dir(datetime)) #Vemos las opciones de datetime, junto con sus métodos
ahora=datetime.datetime.now()
print(ahora) #Cambia los valores conforme el tiempo en que lo llamamos
print(ahora.replace(minute=0)) #Cambiamos el valor de los minutos
print(ahora.replace(minute=0, second=0, microsecond=0)) #Aquí cambiamos los valores de minuto segundo y microsegundo
ayer=datetime.datetime(2019,12,17) #Pasamos como parámetro el día de ayer
print(ayer)
print(inicio)
print(ahora)
print(ahora-ayer)#Podemos hacer restas con estos objetos
print(ahora.second) #Podemos imprimir solo el segundo
print(ahora.hour) #imprimimos la hora
print(ahora.weekday()) #Imprimimos el día de la semana solo que igual que los arreglos el Lunes empieza en posición 0
print(dir(ahora))
print(ahora.timestamp())
#El timestamp es contador de cada hora, minuto, segundo desde 1970