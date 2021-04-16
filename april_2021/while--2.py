#!/usr/bin/env python
abacaxi = 3
balas = 94


#!/usr/bin/env python
#x = 0
while abacaxi >= 2:
    print("Troca o valor de balas para {}.".format(abacaxi))
    print(("Troca abacaxi para: {} - 1".format(abacaxi,abacaxi)))
    balas = abacaxi
    abacaxi = abacaxi - 1 #abacaxi -= 1
    print ("1º while: abacaxi ={} e balas = {}".format(abacaxi,balas)+"\n")
    continue
while balas <= 2:
    print("Balas é {} + 1".format(balas))
    balas += 1
    
    print("2º while: Valor de balas é {}".format(balas)+"\n")
    continue
operacao = ((2*abacaxi) + (2*balas))
print("Final da operação é {}".format(operacao))