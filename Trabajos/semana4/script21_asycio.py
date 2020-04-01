import asyncio, time

async def cosas_locas(numero_loco, numero_mas_loco):
    start_time = time.time()
    print(f'Buscar números divisibles entre {numero_loco} en rango {numero_mas_loco}')
    elegidos = []

    for numero in range(numero_mas_loco):
        if numero % numero_loco == 0:
            elegidos.append(numero)
        if numero % 5000 ==0:
            await asyncio.sleep(.001)
        
    end_time = time.time()
    print(f'Listo: {numero_loco}\t Tiempo de procesamiento: {end_time - start_time}')
    return elegidos

async def main():
    ciclo1 = ciclo.create_task(cosas_locas(32010, 500090000))
    ciclo2 = ciclo.create_task(cosas_locas(52010, 80000))
    ciclo3 = ciclo.create_task(cosas_locas(20, 5000))

    await asyncio.wait([ciclo1, ciclo2, ciclo3])
    #Lo que estamos haciendo es hacer la funci+on de los 3 ciclos de cosas locas, después esperarlos con el await pra enviarlos en forma de lista
    return ciclo1, ciclo2, ciclo3

if __name__ == '__main__':
    try:
        ciclo = asyncio.get_event_loop()
        ciclo.run_until_complete(main())
    except Exception as e:
        pass    #No se debe de hacer esto, hace que al buscar el error, lo deja pasar, como si nada hubiera pasado
    finally:
        ciclo.close()