#! python3
 #Break and Else

nomes = ['deise','thomas','iara']
busca = input('Digite o nome de uma pessoa da família: ')

for nomes in nomes: #percorro a lista
     if busca.lower().strip() == nomes:
         print('É integrante da família')
         break
else:
    print('Não é da família')




# #|| Continue
# par = []

# for x in range(20):
#     if x % 2 != 0 :
#         continue
#     par.append(x)
# print(par)



# || Break
# cont = 0
# while cont < 10:
#     print ('Execução {}'.format(cont))
#     if cont == 5:
#         print ('Para look com BREAK')
#         break
#     cont += 1