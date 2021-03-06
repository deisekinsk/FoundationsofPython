#!python3

def ler_arquivo(nome:str)-> list:
    try:
        with open(nome, 'r') as arq:
            return arq.readlines()
    except Exception as e:
        return ['Erro:{}'.format(e)]


def escrever_arquivo(nome:str, conteudo: list)-> bool:
    try:
        with open(nome, a) as arq:
            conteudo = [x+'\n' for x in conteudo]
            arq.writelines(conteudo)
            return True
    except Exception:
        return False

def contar_linhas (nome: str)-> int:
    return len (ler_arquivo(nome))

# print (ler_arquivo('desafia.txt'))
# print (contar_linhas('desafia.txt'))
nomes = ['caja','caju']
print (escrever_arquivo('desafia.txt', nomes))