
matriz = [
[1,2,3],
[4,5,6],
[7,8,9]
]
# percorrer a matriz com FOR. | Enumerate (contador) cria um índice de execução automática gerado por uma variável.
a = 0
b = 0
for x, y in enumerate(matriz):
    #print (x,y) | #print (y[x])
    a += y[x]
    b += y[-(x+1)] #O valor negativo pega os valores de trás para frente. A soma x+1, é para agregar ao índice que inicia em 0.

print(a + b ) #Cuidado com a identação.
    