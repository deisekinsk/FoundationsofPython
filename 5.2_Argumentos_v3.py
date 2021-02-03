
#!python3

#Args e Kwargs. Args converte os parametros em tuplas. E Kwars converte os parametros em dicionário.


def cadastro (**Kwargs):
    print(type(Kwargs)) #criando dicionário

cadastro(nome='Deise', sobrenome ='Kinsk', idade = 32)
exit()


def soma(*num):
    return(sum(num)) #Inserida a função SUM
var = soma(6,7,5)
print(var)
