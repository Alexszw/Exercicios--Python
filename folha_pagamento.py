#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto
#de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS
#corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido
#corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora
#e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
# abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

valor_hora = float(input("Digite o valor da hora trabalhada : "))
qtd_horas = float(input("Digite o número de horas trabalhadas : "))
salario_bruto = valor_hora * qtd_horas
desconto_ir = 0
valor_ir = 0
desc_sindicato = (3 * salario_bruto) / 100
desc_fgts = (11 * salario_bruto) / 100 # Essse desconto a empresa paga
desc_inss = (10 * salario_bruto) / 100
total_desc = 0

if salario_bruto <= 900 :
    valor_ir = 0
    desconto_ir = 0

elif 900 < salario_bruto <= 1500 :
    valor_ir = 5
    desconto_ir = (valor_ir * salario_bruto) / 100

elif 1500 < salario_bruto <=2500 :
    valor_ir = 10
    desconto_ir = (valor_ir * salario_bruto) / 100

elif salario_bruto > 2500 :
    valor_ir = 20
    desconto_ir = (valor_ir * salario_bruto) / 100

total_desc = desc_inss + desconto_ir
salario_liquido = salario_bruto - total_desc


print(f"Salário bruto : ({valor_hora} * {qtd_horas} )      : R$ {salario_bruto}")
print(f"(-) IR  ({valor_ir} % )                      : R$ {desconto_ir}")
print(f"(-) INSS  (10 %)                    : R$ {desc_inss} ")
print(f"FGTS  (11%)                         : R$ {desc_fgts}")
print(f"Total descontos                     : R$ {total_desc} ")
print(f"Salário Liquido                     : R$ {salario_liquido}")


