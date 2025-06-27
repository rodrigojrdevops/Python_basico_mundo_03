#Utilizando Tuplas, as tulpas são imutáveis
#listas 
#dicionários

'''lanche = ["hambúrguer", "suco", "pudim", "batata frita"]
print(f'{lanche}')


for c in lanche:
    print(f'{c}')
'''

#Pratica

'''lanche = ('Hambúrger', 'suco', 'Pizza', 'Pudim')
print(f'{lanche}')'''

'''lanche = ('Hmabúrguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche))
    print(f'Eu vou comer {lanche[cont]}')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''

'''for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5, 1))'''

pessoa = ('Rodrigo', 39, M, 99.88)
del(pessoa)
print(pessoa)