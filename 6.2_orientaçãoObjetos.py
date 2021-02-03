#! python3


#Requisitos da orientação a objetos 1- Abstração; 2- Encapsulamento; 3- Henrança; 4- Polimorfismo. Vantagens da Orientação a objetos: Reutilização do código; Escalabilidadea; Manutenibilidadea; Agilidade no desenvolvimento.
# CLASS definem propriedades e métodos. Classe não é um objeto.

class Dog:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 10
        self.sede = 10
        self.fome = 10
    def latir(self):
        self.sede -= 1
        print('Latindo...')
    def andar(self):
        self.energia -= 1
        self.fome -= 1
        self.sede -= 1
        print('Andando...')
    def dorrmir(self):
        self.energia = 10
        print('Dormiu')
    def beber (self):
        print('Bebeu.')
    def comer (self):
        self.fome = 10
        print('Comendo...')
dog1 = Dog ('Biu', 'Viralata', 2)

# print (dir(dog1.__doc__))   #Emite a docmentação do objeto 

print (dog1.nome, dog1.raca, dog1.idade, sep=', ', end=" anos.")

for x in range(2):
    dog1.comer()
    dog1.andar()



print(dog1.nome,'''
    energia {}
    fome {}
    sede {}
'''.format(dog1.energia, dog1.fome, dog1.sede, sep='\n'))
