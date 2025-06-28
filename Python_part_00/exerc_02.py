#Fatiamento e acesso a tuplas

#Crie uma tupla preechida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de futebol, na ordem de colocação.Depois mostre:
#Os 5 primeiros.
#Os últimos 4 colocados
#Times em ordem alfabética.
#Em que posição está o time da Chapecoense.

times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio', 
         'Cruzeiro', 'Flamengo', ' Vasco', 'Chapecoense', 
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos que estão na zona de rebaixamento são {times[-4:]}')
print('-= ' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-= ' * 15)
print(f'A chapecoense está na {times.index("Chapecoense")+1}ª')


