import re

def es_rfc_valido(expresion):
    regex = r'^[A-Z]{4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[A-Z|\d]{3}$'

    if re.search(regex, expresion):
        return f'{expresion} Si es una RFC válida.'
    else:
        return f'{expresion} No es una RFC válida.'

print(es_rfc_valido('MELM8305281H0'))
print(es_rfc_valido('MELM8328051H0'))
print(es_rfc_valido('M3LM8305281H0'))
print(es_rfc_valido('MELM8305281H0LA'))

#Cuatro letras mayúsculas = [A-Z]{4}
#Dos números que marcan el año = [0-9]{2}
#Para el mes serán dos números pero del 1 al 12 = 0[1-9]  ->Por ejemplo Febrero es 02
                                                # 1[0-2]  ->Para los meses como Octubre o Diciembre
#Para el día igual son dos núemros pero con rango del 1 al 31
#   0[1-9] ->Primeros días del 1 al 9
#   1[0-9] ->Días del 10 al 19
#   2[0-9] ->Días del 20 al 29
#   3[0-1] ->Días del 30 al 31
#Clave del SAT  ->[A-Z|\d]{3}