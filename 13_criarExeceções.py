#! python3

#Raise Exception: Criar próprias exceções sem parar a execução.

var = input ('Qual a melhor linguagem de programação? ')

try:
    if var.lower().strip() == 'python':
        print ('Você acertou!')
    else:
        raise ValueError ('Linguagem errada!')
except ValueError as e:
    print ('ERRO: {}'.format(e))