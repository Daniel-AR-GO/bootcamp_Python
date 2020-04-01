cadena= 'hello World!'
lista=list(cadena) #Convertimos el elemento en una lista
print(lista)
iter(cadena)
iter(lista)
l= iter(lista)
print(next(l))
print(next(l))
print(lista)
lista.pop(5) #Elimina un elemento en la posición que indicamos
print(lista)
lista.insert(0, '¡') #Agrega un elemento pero se necesita especificar posición
print(lista)
lista.append('!')   #Agrega ul elemento a la cadena pero al final
print(lista)
copia=lista.copy()  #Copia los elementos de la lista
print(copia)
copia.clear() #Elimina los elementos de la lista
print(copia)
print(lista.count('o')) #Cuenta los elementos que sean idénticos al parámetro
print(lista.count('W'))
lista.remove('!') #Elimina el primer elemento que es idéntico al parámetro
print(lista)
lista.remove('o')
print(lista)
lista.sort() #Ordena los elementos en orden Alfabético
print(lista)
lista.reverse() #Ordena los elementos de fin a inicio
print(lista)