#!python3
#Herança utiliza os dados das classes entre si. Necessário para a programação orientada a objetos. É possível herdar mais de uma classe.#Polimorfismo significa muitas formas.

class Car ():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 'gasolina'

    def acelerar (self):
        print('Carro em aceleração...')

    def freiar (self):
        print('Pisou no freio.')

class Car_eletric(Car):
    def __init__(self,marca, modelo, ano):
        super().__init__(marca,modelo,ano)
        self.combustivel = 'elétrico'
    def acelerar(self):
        print('Carro elétrico não "arranca".')

varCar = Car ('Monza', 'GL', 1990)
varCarEletric = Car_eletric('Chevrolet', 'Bolt', '2018')

print(varCar.modelo, varCar.combustivel, sep=',', end='.')
varCar.freiar()
print(varCarEletric.modelo, varCarEletric.combustivel, sep=',', end='.')
varCarEletric.acelerar()