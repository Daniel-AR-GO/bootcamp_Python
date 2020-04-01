numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
pares = list(filter(lambda n: n%2 ==0, numeros))
print(pares)
nones = list(filter(lambda n: n%2 !=0, numeros))
print(nones)
from random import random
print(random()) #Para obtener números random con decimales
print(random())
print(random())
from random import randint
print(randint(1,5)) #Para obtener números random enteros pero debe tener un rango
print(randint(1,5))
print(randint(1,5))
base = randint(1,40)
print(base)
lista = []
for n in range(1,10): #Estamos obteniendo 9 números aleatorios
    lista.append(randint(1,40))
print(lista)
mayor = list(filter(lambda n: n>base, lista))
menor = list(filter(lambda n: n<base, lista))
print(base)
print(mayor)
print(menor)
password = ['xqqtmi1p', 'r360', 'zmkWdUr630', 'PGGPX2', '6RZiUbkk2sdsi', 'j9eIeeWgF', '0siegsye5kkl']
print(password)
validos = list(filter(lambda p: len(p)>7, password))
print(validos)
numeros = [(5,2), (5,3), (5,4), (5,5), (5,8)]
potencias = list(map(lambda x: x[0]**x[1], numeros))
print(potencias)