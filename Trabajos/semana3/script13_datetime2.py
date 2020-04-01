import datetime
ahora= datetime.datetime.now()
print(ahora.timestamp())
print(ahora.microsecond)
print(ahora.year)
print(ahora.month)
print(ahora.strftime('%B'))
print(ahora.strftime('%b'))
print(ahora.strftime('%m'))
fecha= f'Actopan, Hidalgo a {ahora.strftime("%d")} de {ahora.strftime("%B")}, de {ahora.strftime("%Y")}'
print(fecha)
tw = f'{ahora.strftime("%I")}:{ahora.strftime("%M")} {ahora.strftime("%p")} . {ahora.strftime("%b")} {ahora.strftime("%d")}, {ahora.strftime("%Y")}'
print(tw)
tw = f'{ahora.strftime("%I:%M %p")} . {ahora.strftime("%b %d, %Y")}'
print(tw)