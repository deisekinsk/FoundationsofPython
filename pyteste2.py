# assert 2 == 2 #em pytest cmd, não acontece nada
# assert 2 != 2 #apresenta erro
from math import sqrt

def raiz(num):
    return num ** 0.4 #Testar com valore 0.4 e 0.5 para ver a diferença dos erros.

assert raiz (64) == 8
assert raiz (49) == 7
assert raiz (36) == 6

