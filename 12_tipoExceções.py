#! python3

#Exception Types para verificar exceções. Usar com TRY/EXCEPT. Semelhante ao bloco IF/ELIF.

# try:
#    5/0
#    except ZeroDivisionError:
#     print('Não pode dividir número de zero.')

listaProdutos = [
    {'nome': 'produto1', 'valor': 2.0},
    {'nome': 'produto2', 'valor': 1.0},
    {'nome': 'produto3', 'valor': 2.5},
    {'nome': 'produto4', 'valor': 3.0},
]

try:
    for produto in listaProdutos:
        produto ['valor'] += produto['valor'] * 0.1
except KeyError as e:
    print('Chave não pertence ao produto: {}'. format(e))
except Exception as e:
    print('Erro: {}'.format(e))
finally:
    print(listaProdutos)