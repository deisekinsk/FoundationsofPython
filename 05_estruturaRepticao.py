#! python3
#
#Recebe numero inteiro digitado no terminal
idade = int(input('Quantos anos você tem? '))
habilitacao = input('Você possui CNH? ')
dirigir = False
#LOWER deixara a string em minúsculo. STRIP tira os espaço antes e no final. Para assim igualar a condição proposta que é 'sim'.
#
#Primeiro bloco de condição
if habilitacao.lower().strip() == 'sim':
    habilitacao = True
else:
    instrutor = input('Você tem um instrutor de condução? ')
    if instrutor.lower().strip() == 'sim':
        dirigir = True
#
#Segunda bloco de condição. | Encadeamento de condição usa ELIF
if idade >= 18 and habilitacao == True:
    print('Você pode dirigir!')
elif dirigir:
    print ('Boa aula!')
else:
    print('Você não pode dirigir...fon fon fon.')
