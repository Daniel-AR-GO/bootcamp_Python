def pepepecas(tupla):
    pe = tupla[0].upper(), tupla[1].upper()
    pecas = tupla[0], tupla[1], tupla[2], tupla[3], tupla[4]
    pica = tupla[0].upper(), tupla[5].upper(), tupla[2].upper(), tupla[3].upper()
    papas = tupla[0], tupla[3], tupla[0], tupla[3], tupla[4]
    sep = (' ',)
    trab1 = list(pe*2 + sep + pecas + sep + pica + sep + papas + sep + papas + sep + pica + sep + pecas + sep + pe*2)
    trabalenguas = (''.join(trab1))
    return trabalenguas

tupla = ('p','e', 'c', 'a', 's', 'i')
print(pepepecas(tupla))
#PEPE pecas PICA papas papas PICA pecas PEPE