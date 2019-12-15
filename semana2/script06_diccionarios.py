perro = {'nombre':'Lilo', 'edad':8, 'color':'negro', 'raza':'Pastor Aleman'}
#Un diccionario almacena llaves y valores
print(perro)
perro2 = perro.copy() #Copiamos los valores del diccionario
print(perro2)
perro2.clear() #Eliminamos los valores del diccionario
print(perro2)
perro['pasatiempo']='dormir'
print(perro)
perro['ladrido']='agudo'
print(perro)
perro.popitem() #Elimina el último valor del diccionario
print(perro)
perro['edad']=9 #Editamos el contenido de esta llave
print(perro)
perro.pop('edad') #Eliminamos una parte del diccionario
print(perro)
print(perro.get('nombre'))
tupla =('llav1', 'llav2', 'llav3')
lista = [1, 2]
print(dict.fromkeys(tupla, lista))
print(perro.keys())
for elemento in perro:  #Aquí solo imprime los keys
    print(elemento)
for elemento in perro.values(): #Aquí imprime los valores de los keys
    print(elemento)
for elemento in perro.items(): #Aquí se imprime key & valor
    print(elemento)
print(len(perro))
if 'pasatiempo' in perro:
    print(perro['pasatiempo'])
perro2 = perro.copy()
perro3 = perro.copy()
perro4 = perro.copy()
perro2['nombre']='Robin'
perro3['nombre']='Mila'
perro4['nombre']='Rufus'
print(perro)
print(perro2)
print(perro3)
print(perro4)
familia = {'perro1':perro, 'perro2': perro2, 'perro3': perro3, 'perro4': perro4}
print(familia)
print(familia['perro4']['nombre']) #Así se imprime valores específicos