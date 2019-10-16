#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
#varia entre 0 e 25,26 e 60 e maior que 60 e então dizer se a turma é jovem, adulta ou idosa conforme a média calculada.
numero_pessoas = int(input('Digite o número de pessoas :'))
total_idades = 0
for n in range(0,numero_pessoas) :
    if numero_pessoas >= 1 :
        idade = int(input('Qual a sua idade :'))
        total_idades += idade
    else :
        print('Número de pessoas inválido !')
media = total_idades/numero_pessoas
if media >= 0 and media <= 25 :
    print(f'A turma é jovem tem idade média de {media} anos ')
elif media >= 26 and media <= 60 :
    print(f'A turma é adulta tem idade média de {media} anos')
elif media > 60 :
    print(f'A turma tem idade media de {media} anos ')
else :
    print('Média incorreta !')
