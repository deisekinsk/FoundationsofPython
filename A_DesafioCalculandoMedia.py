# notas = [10, 6, 9.5, 2.5]

# for notas in notas:
#     if notas >= 7:
#         print ('Aprovado')
#     elif notas > 3:
#         print ('Recuperação')
#     else:
#         print ('Reprovado')

soma = 0

for x in range (4):
    try:
        notas = float(input('Digite notas {}: '.format(x+1)))
        if notas > 10:
            raise ValueError('Não existe nota maior que a 10.')
        soma += notas
    except ValueError as e:
        print(e)

media = soma /4

if media >= 7:
    print ('Nota {}, aprovado!'.format(media))
elif media > 3:
    print ('Nota {}, recuperação'.format(media))
else:
    print ('Nota {}, reprovado'.format(media))

