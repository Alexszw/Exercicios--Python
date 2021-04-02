#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
#e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de
#Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo
valor_hora = float(input("Digite o valor da sua hora em R$ : "))
numero_horas = float(input("Digite o número de horas trabalhadas :"))
salario = valor_hora * numero_horas
inss = (salario * 8) / 100
imposto = (salario * 11) / 100
sindicato = (salario * 5) / 100
print(f"salario bruto : R$ {salario}")
print(f"Valor do inss : R$ {inss}")
print(f"valor do sindicato : R$ {sindicato}")
print(f"Valor do IR : R$ {imposto}")
print(f"Salário liquido : R$ {salario - (inss + imposto + sindicato)}")


