#Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de ero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('Zero', 'um', 'dois', 'três', 'quatro', 
        'cinco', 'seis', 'sete', 'oito', 'nove', 
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito', 
        'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[núm]}')
