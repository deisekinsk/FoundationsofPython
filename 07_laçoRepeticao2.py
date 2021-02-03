#WHILE permite execução de um bloco de código, deixa que o parâmetro seja verdadeira. | Contador x += 1 (signigica x = x + 1)
#! python3
#WHILE TRUE cria um loop infinito, dizendo que a condição é sempre verdadeira.

aux = True #AUX é o controle do loop.
x = 1 # X é o contador.
while aux:
    print('Conferindo a execução {}'.format(x))
    if x == 15:
        aux = False #Para o loop quando identifica 15.
    x += 1
print('Fim do laço de repetição.')

