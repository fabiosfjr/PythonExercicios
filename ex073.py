#Crie um tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
#Depois mostre:
#A) Apenas os 5 primeiros colocados;
#B) Os ùltmos 4 colocados da tabela;
#C) Um lista com os times em ordem alfabética;
#D) Em que posição da tabela está o time da Chapecoense.
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem Alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição') # "Chapecoense" está com duas aspas, pois já tem uma aspa dentro do f

