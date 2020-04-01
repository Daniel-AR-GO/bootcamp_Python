def pares(inicio, final):
    for par in range(inicio, final+1):
        yield par
g = pares(4,60)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(list(g))

import time
def pares():
    print(f'Entro a la función')
    time.sleep(10)
    print(f'Salió de la función')
pares()

import asyncio
async def funcion():
    print(f'Hola, entró a la función')
    await asyncio.sleep(4)
    print(f'Salió')
asyncio.run(funcion())