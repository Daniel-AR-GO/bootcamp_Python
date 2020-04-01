def funcion(n1,n2,n3):
    return n1+n2+n3
print(funcion(2,4,6))
lambda n1, n2, n3 : n1+n2+n3
suma = lambda n1, n2, n3 : n1+n2+n3
print(suma(2,4,6))
n_potencia = lambda num, n: num**n
print(n_potencia(5,2))
print(n_potencia(5,8))
n_potencia = lambda num, n=2: num**n #Esto es para que tome un valor por default si es que no le damos
print(n_potencia(2))
print(n_potencia(4,6))
genios = ['Leonardo da Vinci', 'Marie Curie', 'Katherine Johnson', 'Albert Einstein', 'Johann Wolfgang von Goethe', 'Ada Lovelace']
genios.sort()
print(genios) #Está opción nos permite ordenar los elementos por orden alfabético
genios.sort(key= lambda nombre: nombre.split()[1]) #Aquí ordenaremos pero por apellidos
print(genios)
genios.sort(key= lambda nombre: nombre.split()[-1])
print(genios)