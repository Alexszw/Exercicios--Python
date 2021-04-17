# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

dia = int(input("Digite o valor correspondente ao dia da semana : "))
if dia == 1:
    print(f"{dia} - Segunda")

elif dia == 2:
    print(f"{dia} - Terça ")

elif dia == 3:
    print(f"{dia} - Quarta")

elif dia == 4:
    print(f"{dia} - Quinta")

elif dia == 5:
    print(f"{dia} - Sexta")

elif dia == 6:
    print(f"{dia} - Sábado")

elif dia == 7:
    print(f"{dia} - Domingo")

else:
    print(f"{dia} - Valor inválido !")
