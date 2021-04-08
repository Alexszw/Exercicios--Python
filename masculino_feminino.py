#Faça um Programa que #verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.
letra = str(input("Digite a letra correspondente ao sexo : "))
letra = letra.upper()
if letra == "F" :
    print(f"{letra} - Feminino")
elif letra == "M" :
    print(f"{letra} - Masculino")
else :
    print("Sexo inválido.")
