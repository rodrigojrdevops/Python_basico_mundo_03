#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre-os:
#Quantas vezes apareceu o valor 9
#Em que posição foi digitado o primeiro valor 3.
#Quais foram os números pares.

num = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+ 1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
for n in num:
    if n % 2 == 0:
        print(n, end='')
