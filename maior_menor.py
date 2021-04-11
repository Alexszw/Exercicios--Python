#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input("Digite um número : "))
num2 = float(input("Digite outro número : "))
num3 = float(input("Digite outro número : "))

if num1 >= num2 >= num3 :
    print(f"O maior número digitado foi o número {num1} e o menor foi o número {num3}")
elif num1 >= num3 >= num2 :
    print(f"O maior número digitado foi o número {num1} e o menor foi o número {num2}")
elif num2 >= num1 >= num3 :
    print(f"O maior número digitado foi o número {num2} e o menor foi o número {num3}")
elif num2 >= num3 >= num1 :
    print(f"O maior número digitado foi o número {num2} e o menor foi o número {num1}")
elif num3 >= num2 >= num1 :
    print(f"O maior número digitado foi o número {num3} e o menor foi o numero {num1}")
else :
    print(f"O maior número digitado foi o número {num3} e o menor foi o número {num2}")
