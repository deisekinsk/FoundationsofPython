
#!python3

#Args e Kwargs. Args converte os parametros em tuplas. E Kwars converte os parametros em dicionário.


def cadastro (**Kwargs):
    print('A usuária {} {}, é de maior ({} anos) e foi cadastrada com sucesso!'.format(Kwargs['nome'],Kwargs['sobrenome'],Kwargs['idade'])) #mensagem personalizada

cadastro(nome='Deise', sobrenome ='Kinsk', idade = 32)
exit()


def soma(*num):
    return(sum(num)) #Inserida a função SUM
var = soma(6,7,5)
print(var)
