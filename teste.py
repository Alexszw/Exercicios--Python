print('***************************************************')
print('********** Bem vindo ao jogo da advinhação ********')
print('***************************************************')
chute = int(input('Digite um número :'))
numero_secreto: int = 23
for n in range(1, 3):
	if chute == numero_secreto:
		print('Você acertou !')
		break
	else :
		print('Você errou !')
		chute = int(input('Digite novamente :'))
