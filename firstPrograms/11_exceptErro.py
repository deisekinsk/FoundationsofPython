#! python
num = input('Digite um número: ')

try:
    print(int(num) + 2)#importante converte para inteiro INT
except Exception:
    print('não é um número')