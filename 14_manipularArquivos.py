#! python3

# Para trabalhar com arquivos, será necessário criar um objeto que disponibiliza os métodos READ ou WRITE. Existem duas formas de criar objetos de arquivo: binários e de textos.

#OPEN() é a sintaxe para abrir o arquivo. Seguindo o padrão open(nome_arquivo, 'modo'). Sendo que para modo, pode ser leitura ou escrita.

# W abre o arquivo

arquivo = open('frutas.txt', 'w')

arquivo.write('laranja')

arquivo.close()

