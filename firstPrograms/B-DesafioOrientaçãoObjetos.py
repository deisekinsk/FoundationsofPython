#! python

class Conta ():
    def __init__(self, titular, numero, saldo): #defini os PARAMETROS
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
    
    def sacar (self, valor): #definindo MÉTODOS
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def transferir(self, valor, conta):
        self.sacar(valor)
        conta.depositar(valor)

class Poupança (Conta): #Recebe a henrança de CONTA
    def __init__(self, titular, numero, saldo):#sobreescrevendo os dados da classe pai
        super().__init__(titular, numero,saldo)#trazendo de volta
        self.juros = 0.0100 #Juros atributo fixo

    def renderJuros(self):
            self.saldo += self.saldo * self.juros


varConta1 = Conta('Deise', 167289,1500 )
varConta2 = Poupança('Thomas', 167289,1500 )

varConta1.sacar(100)
varConta1.transferir(500, varConta2)

varConta2.renderJuros()
varConta2.sacar(20)


print(varConta1.saldo, varConta1.titular, sep=', ', end='. \n')
print(varConta2.saldo, varConta2.titular, sep=', ', end='.')



