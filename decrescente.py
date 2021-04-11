#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input("Digite um número : "))
n2 = float(input("Digite outro número : "))
n3 = float(input("Digite outro número : "))

if n1 >= n2 >= n3 :
    print(f"Os números em ordem decrescente são : {n1, n2, n3}")

elif n1 >= n3 >= n2 :
    print(f"Os números em ordem decrescente são : {n1, n3, n2}")

elif n2 >= n1 >= n3 :
    print(f"Os números em ordem decrescente são : {n2, n1, n3}")

elif n2 >= n3 >= n1 :
    print(f"Os números em ordem decrescente são : {n2, n3, n1}")

elif n3 >= n2 >= n1 :
    print(f"Os números em ordem decrescente são : {n3, n2, n1}")

else :
    print(f"Os números em ordem decrescente são : {n3, n1, n2}")