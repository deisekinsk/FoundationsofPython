#  #Pergunta 8 - Considere o código 3. Para que a funcao_3 realize o “print” de caracteres de uma string presente nos índices ímpares, qual pode ser uma possível alteração no código original?  

# def funcao_3(str):
#     for i in range(1, len(str)-1,2):
#         print("Índice[",i,"]", str[i])

# funcao_3('ABDCEFGHIJKLMNOPQ')

# #Código 4
# def funcao_4(lista_numerica):
#     print("Valor Passado", lista_numerica)

#     a = lista_numerica[0]
#     b = lista_numerica[-1]
#     if (a == b):
#         return True
#     else:
#         return False
# numeros = [10,20,30,40,10]

# funcao_4(numeros)

# def funcao_da_classe_1(self, string):
#     dicionario = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500,          'M' : 1000,}
#     valor = 0
#     for i in range(len(string)):
#         if i > 0 and dicionario[string[i]] > dicionario[string[i-1]]:
#             valor += dicionario[string[i]] - 2 * dicionario[string[i-1]]
#         else:
#             valor += dicionario[string[i]]
#     return valor

# print(funcao_da_classe_1(0,'XXXVII'))

# tupla_1 = tuple('KINSK')
# print('Resultado: \n', (tupla_1), '\n','O penúltimo elemento é: ', (tupla_1 [-1]))

a_b_c= 1,000,000
print(type(a_b_c))

a b c = 1000 2000 3000. 
pritn(a b c)