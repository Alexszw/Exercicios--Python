#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
# V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.

turno = str(input("Digite o turno que você estuda sendo M-matutino, V-Vespertino, N-noturno : "))
turno = turno.upper()
if turno == "M" :
    print("Bom Dia!!")
elif turno == "V" :
    print("Boa Tarde!!")
elif turno == "N" :
    print("Boa Noite!!")
else :
    print("Valor Inválido!!")