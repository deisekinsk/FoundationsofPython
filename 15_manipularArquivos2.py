#! python3

# Para trabalhar com arquivos, será necessário criar um objeto que disponibiliza os métodos READ ou WRITE. Existem duas formas de criar objetos de arquivo: binários e de textos.

#OPEN() é a sintaxe para abrir o arquivo. Seguindo o padrão open(nome_arquivo, 'modo'). Sendo que para modo, pode ser leitura ou escrita.

# W abre o arquivo,  R faz leitura do arquivo

# \n quebra linha

#cria o arquivo e escreve
with open('frutas.txt', 'w') as arquivo:
    arquivo.write('jaca\n')
    arquivo.write('laranja')

#Para ler o arquivo. READ para leitura. READLINES volta a lista. :

with open('frutas.txt', 'r') as arquivo:
    print (arquivo.readlines())
