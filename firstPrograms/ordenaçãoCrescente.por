programa
{
	//Declaro as variáveis com seus números inteiro.
	//Variável temporária. 
	inteiro n1, n2, n3, n4,t
	//ordena 4 números em ordem crescente
	funcao inicio()
	{
		//Entra Valores
		escreva("Digite o primeiro número: ")
		leia(n1)

		escreva("Digite o primeiro número: ")
		leia(n2)

		escreva("Digite o primeiro número: ")
		leia(n3)

		escreva("Digite o primeiro número: ")
		leia(n4)

	//Compara valores com faca/enquanto
faca compara () {
		
		se (n1 > n4) {
			t = n1
			n1 = n2
			n2 = t
		}

		
		se (n2 > n3) {
			t = n2
			n2 = n3
			n3 = t
		}

		
		se (n3 > n4) {
			t = n3
			n3 = n4
			n4 = t
		}
		
}enquanto{n1 > n4 ou n1 >n2 ou n2>n3 ou n3>n4}
	
	escreva (n1,n2,n3,n4)
	
	}
	
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 703; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */