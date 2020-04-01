import re
cadena = 'pepe pecas pica papas pica papas pepe pecas'
print(re.findall(r'pepe', cadena)) #Busca en nuestra cadena la palabra pepe
print(re.findall(r'p', cadena))
print(re.findall(r'\bp', cadena)) #\b esta expresión busca a la p pero que antes tenga un espacio
print(re.findall(r'\bp[a-z]*', cadena)) #Aquí estaremos buscando que exista un espacio entre la p, pero que además adelante tenga letras de a-z, el asterisco muestra que no importa cuantos valores existan después
print(re.findall(r'\bp[a-z]{1,3}', cadena)) #Estamos haciendo lo mismo que antes pero ahora solo mostraremos las 3 primeras letras
cadena = 'pepe pecAs pica pApAs picA papas pepe pecas'
print(re.findall(r'\bp[a-z]*', cadena)) #Aquí veremos que se rompe el proceso por las letras mayúsculas
print(re.findall(r'\bp[A-Z]*', cadena)) #Aquí también se romperá porque buscará forzosamente con mayúsculas después de la p
print(re.findall(r'\bp[A-z]*', cadena)) #Esta es la forma correcta para evitar que se rompa el proceso
cadena = 'pepa pecas pica papas pica papas pepe pecas'
print(re.findall(r'\bpep[ae]*', cadena)) #No damos intervalo con la ae, si no que damos dos opciones
print(re.findall(r'\bpep[a]*', cadena))
cadena = 'pepe pecas. pica papas.'
print(re.findall(r'.', cadena)) #Esta expresión nos mostrará toda la cadena, porque todo lo considera como puntos
print(re.findall(r'\.', cadena)) #Aquí impriremos correctament el punto
print(re.findall(r'\.\s', cadena))
print(re.findall(r'[\.\s]', cadena))
print(re.findall(r'[a-z]', cadena))
print(re.findall(r'[a-z\s]', cadena))