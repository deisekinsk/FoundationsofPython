x = 4
if x > 5:
    #raise para saber o tipo de erro
    raise Exception ('O valor {}'.format(x))
print('rodou!')

#TryException

try:
    numero = int(input('Entre com um número de 0 a 10.\n'))
except ValueError:
    print('Use um número inteiro.')
    exit(0)

try:
    if (numero%2) == 0:
        print("Par")
    else:
        print("Ímpar")
except Exception:
    print ('Erro!')