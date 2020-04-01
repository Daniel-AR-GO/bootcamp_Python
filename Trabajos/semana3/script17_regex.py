import re

def regex_phone(expresion):
    expresion = re.sub(r'\W+', '', expresion)
    if re.search(r'^55\d{8}$', expresion):
        return f'{expresion} SI es un número válido.'
    else:
        return f'{expresion} NO es número válido.'

print(regex_phone('5566668877123456'))
print(regex_phone('55a - 6666 - 8877'))
print(regex_phone('55-6666-8877'))
print(regex_phone('55.6666.8877'))
print(regex_phone('(55)6666-8877'))
print(regex_phone('45.66.66.8877'))

print('')

def regex_email(expresion):
    regex = r'^[A-z0-9.+-_]+@[A-z0-9-]+\.[A-z0-9-.]+$'

    if re.search(regex, expresion):
        return f'{expresion} SI es un email válido.'
    else:
        return f'{expresion} NO es un email válido.'

print(regex_email('me@katialira.com'))
print(regex_email('esteESUNmail@deprueba.net'))
print(regex_email('no'))
print(regex_email('1234@1password.rest'))

print('')

def regex_password(expresion):
    regex = r'^(?=.{8,}$)' #Para tomar en cuenta que sólo sean 8 carácteres o más, para eso es la coma -> ?=. estos símbolos se llaman como lookahead
    regex = r'^(?=.{8,}$)(?=.*[a-z])' #Para buscar que al menos exita una letra minúscula
    regex = r'^(?=.{8,}$)(?=.*[a-z])(?=.*[A-Z])' #Para buscar que al menos exita una letra MAYÚSCULA
    regex = r'^(?=.{8,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])' #Buscar que al menos exista un dígito
    regex = r'^(?=.{8,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$'
    if re.match(regex, expresion):
        return f'{expresion} SI es una contraseña válida'
    else:
        return f'{expresion} NO es una contraseña válida'

print(regex_password('test'))
print(regex_password('testtest'))
print('')
print(regex_password('TESTTEST'))
print(regex_password('TESTtEST'))
print('')
print(regex_password('testesto'))
print(regex_password('testestO'))
print('')
print(regex_password('testestO'))
print(regex_password('testes7O'))
print('')
print(regex_password('testes7O'))
print(regex_password('testes7O.'))