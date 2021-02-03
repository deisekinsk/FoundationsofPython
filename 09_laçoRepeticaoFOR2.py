#FOR perfeita para trabalhar com listas no python. Trabalha com formato limitado de dados, aonde começa e termina.
#! python3
#RANGE pode orgnaizar números inclusivos e excludentes. Além de poder definir. Estrutura do RANGE (inicio, fim, incremento)
 
# for x in range(0,10, 2):
#     print (x)
letras = []
maiusculas = []
for x in range(97,97 + 26): 
    letras.append(chr(x))
    maiusculas.append(chr(x).upper())
print(letras)
print(maiusculas)
