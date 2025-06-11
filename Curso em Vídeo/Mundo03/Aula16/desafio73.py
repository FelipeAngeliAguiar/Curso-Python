'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem da colocação. Depois mostre:
    A) Apenas os 5 primeiros colocados.
    B) Os últimos 4 colocados da tabela.
    C) Uma lista com os times em ordem alfabética.
    D) Em que posição na tabela está o time da Chapecoense (nn tem ent vai o Grêmio).'''
    
times = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Fluminense', 
         'Botafogo', 'Bahia', 'Mirassol', 'Atlético-MG', 'Ceará SC', 
         'Corinthians', 'Grêmio', 'São Paulo', 'Internacional', 'Vasco da Gama', 
         'EC Vitória', 'Fortaleza', 'Santos', 'Juventude', 'Sport Recife')

print(f'Estatisticas:')
print(f'Lista de times do Brasileirão: \n{', '.join(times)}\n{'=-'*20}')
print(f'Os 5 primeiros colocados são: \n{', '.join(times[:5])}\n{'=-'*20}')
print(f'Os 4 últimos colocados são: \n{', '.join(times[-4:])}\n{'=-'*20}')
print(f'Os times em ordem alfabética: \n{', '.join(sorted(times))}\n{'=-'*20}')
print(f'Grêmio está em: \n{times.index('Grêmio')+1}° lugar\n{'=-'*20}')