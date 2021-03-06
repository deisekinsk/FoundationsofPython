
#!python3

#Args e Kwargs. Args converte os parametros em tuplas. E Kwars converte os parametros em dicionário.

def soma1(*args):
    print(type(args)) #Para ver os valores printados, tire o TYPE e as paranteses. O Type mostra que ele foi convertido pelo ar e agora pertence a classe tupla.
soma1(6,7,5)
