cadena = 'hello World!'
print(cadena)
tupla =tuple(cadena)    #Una tupla es muy similar a las listas pero en estas no se puede cambiar su contenidon ni sus elementos
print(cadena)
print(tupla.count('o'))
print(tupla[2])
print(tupla[-1])
print(tupla[-2])
t=list(tupla)   #Convertimos a lista la tupla para poder editar su contenido
print(t)
t[0]='H'    #Vamos a cambiar el valor de la posición 0
print(t)
tupla= tuple(t)
print(tupla)
tupla = ('php', 'python', 'c', 'c++', 'java', 'javascript', 'html', 'css')
print(tupla)
for lenguaje in tupla:
    print(lenguaje)
if 'python' in tupla:
    print('Si es un lenguaje')
print(len(tupla))
unica =('elemento1',) #Las tuplas se caracterizan por llevar una coma después del elemento
del unica   #Esta función borra los elementos
tupla2= ('r', 'go')
lenguajes= tupla + tupla2
print(lenguajes)
print(lenguajes.index('python')) #Nos da la posición del elemento que sea idéntico al parámetro