print('')
print('Linea de texto\n'.rstrip())

import os
os.getcwd() #Obtiene la dirección en la que estamos
#os.mkdir('test')   Esta opción nos permite crear directorios
usuario = 'katia'
print(usuario)
print('Hola ', usuario, ' bienvenido!')
print('Hola {usuario} bienvenido!')
print(f'Hola {usuario} bienvenido!')
print(f'Hola {usuario*4} bienvenido!')
print(f'Hola {23*4} bienvenido!')
perrito = {'nombre' : 'Lilo', 'pasatiempo' : 'dormir'}
print(f'Mi nombre es {perrito["nombre"]}')
print(f'Mi nombre es {perrito["nombre"]} y me gusta {perrito["pasatiempo"]}')
mensaje = (
    f'Hola! '
    f'Mi nombre es {perrito["nombre"]}'
    f' y me gusta {perrito["pasatiempo"]}'
)
print(mensaje)