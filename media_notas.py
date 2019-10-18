#Faça um programa que calcule o mostre a média aritmética de N notas.
numero_notas = int(input('Qual é o número de notas :'))
soma_nota = float(0)
for n in range(1,numero_notas +1) :
    nota = float(input(f'Digite a {n}° nota :'))
    soma_nota += nota
media = soma_nota/numero_notas
print(f'A média das notas é {media}')