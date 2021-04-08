#Faça um Programa que peça dois números e imprima o maior deles.
numero1 = float(input("Digite um número :"))
numero2 = float(input("Digite outro número :"))
if numero1 > numero2 :
    print(f"O maior número é : {numero1}")
elif numero1 == numero2 :
    print(f"Os números são iguais !")
else :
    print(f"O maior número é : {numero2}")
