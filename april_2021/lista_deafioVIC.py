#Dadas listas X e Y, retorne uma terceira lista (Z) 
#que contenha somente elementos que estão em X e Y. 
#Caso X e Y sejam iguais, Z deverá copiar esses elementos,
#preservando a ordem determinada por X.
# Escreva este algoritmo em qualquer linguagem de sua preferência


# PRIMEIRO: CRIO MINHAS VARIÁVEIS QUE RECEBEM LISTAS
lista_X = ["Deise", "Oroima","Laryssa"]
lista_Y = ["Deise", "Cecília", "Laryssa"]
lista_Z = []


#Aqui ele criou alterou a variável lista_X
lista_X.extend(lista_Y) #Realiza o MÉTODO extend(). Ele adiciona os elementos da lista_Y na lista_X.

#Primeiro criou um dicionário, onde os valores são 'chaves'. Em dicionários, não pode haver duplicação de valores. Por isso, quando passo a nova lista_X por esse dicionário, ele já remove os valores duplicados.
#Por fim, ele converte novamente em uma lista.

lista_X = list(dict.fromkeys(lista_X))

#Lista_Z Recebe nova lista_X
lista_Z = lista_X

print (lista_Z)#Imprimi lista X + lista Y
