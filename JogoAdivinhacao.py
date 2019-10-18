import random
print('***************************************************')
print('********** Bem vindo ao jogo da advinhação ********')
print('***************************************************')
print('Digite a dificuldade do jogo :')
print('Digite (1) para fácil (2) para médio (3) para difícil')
dificuldade = int(input('Qual a dificuldade :'))
numero_secreto = random.randrange(1,101)
numero_tentativas = 0
if dificuldade == 1 :
	numero_tentativas = 20
elif dificuldade == 2 :
	numero_tentativas = 10
elif dificuldade == 3 :
	numero_tentativas = 5
else :
	print('Valor da dificuldade inválido !')

for n in range(1, numero_tentativas):
	print(f'Tentativa {n} de {numero_tentativas}')
	chute = int(input('Digite um número entre 1 e 100 para o chute :'))
	if chute >= 1 and chute <= 100 :
		if chute > numero_secreto:
			print('Você errou ! O número é maior que o número secreto !')
		elif chute < numero_secreto:
			print('Você errou) ! O número é menor que o número secreto !')
		elif chute == numero_secreto:
			print('Você acertou !')
			break
		else :
			print('O número digitado é inválidp !')
			break
	else :
		print('Número inválido !')
		break



