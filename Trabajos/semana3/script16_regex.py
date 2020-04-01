import re
c1 = 'Python es el mejor lenguaje'
c2 = 'Elmejor lenguaje es Python'
c3 = 'Python'
print(re.search(r'Python', c1))
print(re.search(r'Python', c2))
print(re.search(r'Python', c3))
print(re.search(r'^Python', c1)) #Este signo ^ hace que la búsqueda de la palabra solo la busque al inicio
print(re.search(r'^Python', c2)) #Como en esta cadena no esta Python al inicio, nos aparecerá un None
print(re.search(r'^Python', c3))
print(re.search(r'Python$', c1)) #El signo $ hace la búsqueda de la cadena pero ahor al final
print(re.search(r'Python$', c2))
print(re.search(r'Python$', c3))
print(re.search(r'^Python$', c1)) #Ahora con el ^ y el $ hace la búsqueda de inicio al final
print(re.search(r'^Python$', c2))
print(re.search(r'^Python$', c3))
print(re.match(r'^P..n$', 'Python'))  #Lo que hacemos aquí es que al inicio exista la P, después tenga 2 posiciones y termine en n
print(re.match(r'^P....n$', 'Python')) #Aquí si existen las 4 posiciones por lo cual si hará match
print(re.match(r'^P[a-z]n$', 'Python')) #En esta opción mostramos o buscamos una posición que tenga carácter de a-z
print(re.match(r'^P[a-z]*n$', 'Python'))