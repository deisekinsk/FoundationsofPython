#! python3

#funções anônimas. Expressão lâminas, para ajudar funções matemáticas. Lestrutura 'AMBDA argumentos: expressão'

var = lambda x, y: x + y
print (var(77, 29))

#inserindo Lambda dentro do print
print((lambda a: a ** 2)(77))

#Quadrado perfeito dos 10 primeiros números

for b in range(1, 11):
    print ((lambda b: b ** 2)(b))