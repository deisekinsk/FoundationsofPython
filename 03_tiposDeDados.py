#Concatenar Variáveis
nome, idade = 'Deise', 32
msg = 'Ela é {0} e tem {1} anos.'.format(nome,idade)
print(msg)

#Concatenar com operado +. Porém Python não concacatena dados com tipos diferentes. Sendo necessário converter o operador.

msg1= 'Ela é ' + nome + ' e tem ' + str(idade) + ' anos.'
print(msg1)

