# PRIMEIRO: CRIO MINHAS VARIÁVEIS QUE RECEBEM LISTAS
lista_X = ["Deise", "Oroima","Laryssa"]
lista_Y = ["Deise", "Cecília", "Laryssa"]


#Método extend() que une as duas listas sem alterar a orde da lista_X

#lista_Z = lista_X + lista_Y

#Função para remover os repetidos

def remove_repetidos(lista_Z):
    l = []
    for i in lista_Z:
        if i not in l:
            l.append(i)
    #l.sort()
    return l

lista_Z = lista_X + lista_Y

lista_Z = remove_repetidos(lista_Z)

print (lista_X,lista_Y)
print (lista_Z)
