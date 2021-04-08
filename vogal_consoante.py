#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input("Digite a letra :"))
letra = letra.upper()
if letra == "A" or letra =="E" or letra == "I" or letra == "O" or letra == "U" :
    print("A letra digitada é uma vogal.")
else :
    print("A letra diigitada é uma consoante.")