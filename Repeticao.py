1.
Faça
um
programa
que
peça
uma
nota, entre
zero
e
dez.Mostre
uma
mensagem
caso
o
valor
seja
inválido
e
continue
pedindo
até
que
o
usuário
informe
um
valor
válido.

nota = float(input('Digite uma nota entre 0 e 10 :'))
​
while (nota < 0 or nota > 10):
    print('Valor inválido')
    nota = float(input('Digite uma nota entre 0 e 10 :'))
else:
    print('Valor válido !')

Digite
uma
nota
entre
0
e
10: 11
Valor
inválido
Digite
uma
nota
entre
0
e
10: 12
Valor
inválido
Digite
uma
nota
entre
0
e
10: 10
Valor
válido !
2.
Faça
um
programa
que
leia
um
nome
de
usuário
e
a
sua
senha
e
não
aceite
a
senha
igual
ao
nome
do
usuário, mostrando
uma
mensagem
de
erro
e
voltando
a
pedir as informações.

nome = (input('Digite o nome de usuário :'))
senha = (input('Digite a senha de usuário :'))
while (nome == senha):
    print('Valor inválido!A senha tem que ser diferente em relação ao nome!')
    nome = (input('Digite o nome de usuário :'))
    senha = (input('Digite a senha de usuário :'))
else:
    print('Cadastro realizado !')

Digite
o
nome
de
usuário: Al
Digite
a
senha
de
usuário: 12
Cadastro
realizado !
3.
Faça
um
programa
que
leia
e
valide as seguintes
informações:
Nome: maior
que
3
caracteres;
Idade: entre
0
e
150;
Salário: maior
que
zero;
Sexo: 'f'
ou
'm';
Estado
Civil: 's', 'c', 'v', 'd';
while (True):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    salario = float(input('Digite o salário: '))
    sexo = input('Digite o Sexo: ')
    estadocivil = input('Digite o estado civil: ')
    sexo = sexo.upper()
    estadocivil = estadocivil.upper()
    if (len(nome) > 3):
        print('OK')
    else:
        print('Nome inválido!!')
    if (idade > 0 and idade <= 150):
        print('Ok')
    else:
        print('Idade inválida!')
    if (salario > 0):
        print('Ok')
    else:
        print('Salário inválido!')
    if (sexo == 'F' or sexo == 'M'):
        print('ok')
    else:
        print('Sexo inválido!')
    if (estadocivil == "S" or estadocivil == "C" or estadocivil == "V" or estadocivil == "D"):
        print('Ok')
    else:
        print('Estado cívil inválido!')

Digite
o
nome: Alex
Digite
a
idade: 23
Digite
o
salário: 12
Digite
o
Sexo: f
Digite
o
estado
civil: s
OK
Ok
Ok
ok
Ok
4.
Supondo
que
a
população
de
um
país
A
seja
da
ordem
de
80000
habitantes
com
uma
taxa
anual
de
crescimento
de
3 % e
que
a
população
de
B
seja
200000
habitantes
com
uma
taxa
de
crescimento
de
1.5 %.Faça
um
programa
que
calcule
e
escreva
o
número
de
anos
necessários
para
que
a
população
do
país
A
ultrapasse
ou
iguale
a
população
do
país
B, mantidas as taxas
de
crescimento.

pais_a = 80000
pais_b = 200000
ano = 0
​
while pais_a <= pais_b:
    pais_a += pais_a * 0.03
    pais_b += pais_b * 0.015
    ano += 1
​
print(f'O número de anos para que a população do pais A iguale e ultrapasse a população do pais B é : {ano} anos ')





​
O
número
de
anos
para
que
a
população
do
pais
A
iguale
e
ultrapasse
a
população
do
pais
B
é: 63
anos
​
6.
Faça
um
programa
que
imprima
na
tela
os
números
de
1
a
20, um
abaixo
do
outro.Depois
modifique
o
programa
para
que
ele
mostre
os
números
um
ao
lado
do
outro.

for n in range(1, 21):
    print(n)
print(list(range(1, 21)))
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
7.
Faça
um
programa
que
leia
5
números
e
informe
o
maior
número.
for n in range(1, 6):
    numero = float(input('Digite um número :'))
​
if numero > maior:
    maior = numero
print(f'O maior número digitado é {maior} ')

Digite
um
número: 5
Digite
um
número: 4
Digite
um
número: 3
Digite
um
número: 2
Digite
um
número: 1
O
maior
número
digitado
é
5.0
8.
Faça
um
programa
que
leia
5
números
e
informe
a
soma
e
a
média
dos
números.

soma = 0
for n in range(1, 6):
    numero = float(input('Digite um número :'))
    soma += numero

media = soma / 5
print(f'A soma dos número é {soma} e a média é {media}')

Digite
um
número: 1
Digite
um
número: 2
Digite
um
número: 3
Digite
um
número: 4
Digite
um
número: 5
A
soma
dos
número
é
15.0
e
a
média
é
3.0
9.
Faça
um
programa
que
imprima
na
tela
apenas
os
números
ímpares
entre
1
e
50.

for n in range(1, 50 + 1):
    if (n % 2) != 0:
        print(n)
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
10.
Faça
um
programa
que
receba
dois
números
inteiros
e
gere
os
números
inteiros
que
estão
no
intervalo
compreendido
por
eles.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
compara = n1
if compara <= n2:
    while compara <= n2:
        print(compara)
        compara += 1
elif compara >= n2:
    while compara >= n2:
        print(compara)
        compara -= 1

Digite
um
número: 7
Digite
um
número: 1
7
6
5
4
3
2
1
11.
Altere
o
programa
anterior
para
mostrar
no
final
a
soma
dos
números.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
compara = n1
soma = 0
if compara <= n2:
    while compara <= n2:
        print(compara)
        soma += compara
        compara += 1

elif compara >= n2:
    while compara >= n2:
        print(compara)
        soma += compara
        compara -= 1

print(f'A soma dos números é {soma}')

Digite
um
número: 1
Digite
um
número: 4
1
2
3
4
A
soma
dos
números
é
10
12.
Desenvolva
um
gerador
de
tabuada, capaz
de
gerar
a
tabuada
de
qualquer
número
inteiro
entre
1
a
10.
O
usuário
deve
informar
de
qual
numero
ele
deseja
ver
a
tabuada.A
saída
deve
ser
conforme
o
exemplo
abaixo: Tabuada
de
5: 5
X
1 = 5
5
X
2 = 10...
5
X
10 = 50

n1 = int(input('Digite um número entre 1 a 10 para exibir a tabuada :'))
resultado = 0
for n in range(1, 10 + 1):
    resultado = n * n1
    print(f'{n1} X {n} = {resultado}')
Digite
um
número
entre
1
a
10
para
exibir
a
tabuada: 5
5
X
1 = 5
5
X
2 = 10
5
X
3 = 15
5
X
4 = 20
5
X
5 = 25
5
X
6 = 30
5
X
7 = 35
5
X
8 = 40
5
X
9 = 45
5
X
10 = 50
13.
Faça
um
programa
que
peça
dois
números, base
e
expoente, calcule
e
mostre
o
primeiro
número
elevado
ao
segundo
número.Não
utilize
a
função
de
potência
da
linguagem.

base = float(input('Digite o número da base :'))
expoente = int(input('Digite o número do expoente :'))
resultado = 1
multiplica = 0
for n in range(0, expoente):
    multiplica = base * resultado
    resultado = multiplica

print(resultado)
​
Digite
o
número
da
base: 3
Digite
o
número
do
expoente: 3
27.0
14.
Faça
um
programa
que
peça
10
números
inteiros, calcule
e
mostre
a
quantidade
de
números
pares
e
a
quantidade
de
números
impares.

par = 0
impar = 0
for n in range(0, 10):
    n1 = int(input('Digite um número inteiro :'))
    if n1 % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'O número de números pares digitados foi {par} e de números ímpares foi {impar}')

Digite
um
número
inteiro: 2
Digite
um
número
inteiro: 4
Digite
um
número
inteiro: 6
Digite
um
número
inteiro: 8
Digite
um
número
inteiro: 10
Digite
um
número
inteiro: 12
Digite
um
número
inteiro: 14
Digite
um
número
inteiro: 16
Digite
um
número
inteiro: 18
Digite
um
número
inteiro: 20
O
número
de
números
pares
digitados
foi
10
e
de
números
ímpares
foi
0
15.
A
série
de
Fibonacci
é
formada
pela
seqüência
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
Faça
um
programa
capaz
de
gerar
a
série
até
o
n−ésimo
termo.

n1 = int(input('Digite um número para até onde você quer chegar com a série Fibonacci :'))
anterior = 0
posterior = 1
print(posterior, ',', end=' ')
for n in range(0, n1):
    soma = anterior + posterior
    print(soma, ',', end=' ')
    anterior = posterior
    posterior = soma
print('fim....', end=' ')
​


Digite
um
número
para
até
onde
você
quer
chegar
com
a
série
Fibonacci: 4
1, 1, 2, 3, 5, fim.... 