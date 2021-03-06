#! python3

#funções anônimas. Expressão lâminas, para ajudar funções matemáticas. Lestrutura 'AMBDA argumentos: expressão'

quadrado = []

for x in range (1,11):
    quadrado.append((lambda x: x **2)(x))
print(quadrado)
