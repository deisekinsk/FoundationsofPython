#! python3

#Funções em python: DEF cria a função | nome da função com UNDERLINE |paramentros entre parentes e após o DOIS PONTOS os comandos.

nome = 'Anônima (o)' #Variável global

def boas_vindas():
    global nome #Chama variável global
    nome = 'Deise' #Variavel Local
    print ('Seja bem vinda! {}'.format(nome)) #criei a função

boas_vindas() #chamei a função
print (nome) #chamei a variável local
