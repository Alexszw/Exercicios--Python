# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
# seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
altura = float(input("Digite a sua altura : "))
peso_homen = (72.7 * altura) - 58
peso_mulher = (62.1 * altura) - 44.7
print(f"Seu peso ideal para a sua altura de {altura} m é de {peso_homen : .2f} kgs para homens e de {peso_mulher : .2f} kgs para mulheres.")