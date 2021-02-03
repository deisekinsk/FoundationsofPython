#! python3

# with open ('Texto.txt', 'r') as varArquivo:
#     # conteudo = varArquivo.readlines()
#     # print(conteudo)
#     contador = 1
#     for linha in varArquivo:
#        if linha != '\n':
#         # print(linha)
#         print ('{0} - {1}'.format(contador, linha))
#         contador += 1

try:
    with open ('Texto.txt', 'r') as varArquivo:
        # contador = 1
        # conteudo = []
        # for linha in varArquivo:
        #     if linha != '\n':
        #         conteudo.append('{0} - {1}'.format(contador, linha))
        #         contador += 1
        
        conteudo = [var for var in varArquivo if var != '\n']
        for var in range(len(conteudo)):
            conteudo[var] = '{} - {}'.format(var+1, conteudo[var])
        print (conteudo)
    with open ('Texto.txt', 'w') as varArquivo:
        varArquivo.writelines(conteudo)
except FileNotFoundError:
    print('Arquivo não existe.')
except Exception as e:
    print('Error: {}'.format(e))


