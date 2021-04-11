#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Insira o preço do produto : "))
preco2 = float(input("Insira o preço de outro produto : "))
preco3 = float(input("Insira o preço de outro produto : "))

if preco1 >= preco2 >= preco3 :
    print(f"O produto que você deve comprar é o produto de R$ {preco3}")

elif preco1 >= preco3 >= preco2 :
    print(f"O produto que você deve comprar é o produto de R$ {preco2}")

elif preco2 >= preco3 >= preco1 :
    print(f"O produto que você deve comprar é o produto de R$ {preco1}")

elif preco2 >= preco1 >= preco3 :
    print(f"O produto que você deve comprar é o produto de R$ {preco3}")

elif preco3 >= preco1 >= preco2 :
    print(f"O produto que você deve comprar é o produto de R$ {preco2}")

else :
    print(f"O produto que você deve comprar é o produto de R$ {preco1}")
