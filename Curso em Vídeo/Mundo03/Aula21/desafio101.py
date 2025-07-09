'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
    retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''

from datetime import datetime

def voto(ano):
    """
    -> Função para determinar se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO, com base no ano de nascimento.
    :param ano: Ano de nascimento da pessoa.
    :return: Tupla com a idade e a situação do voto.
    """
    
    idade = datetime.now().year - ano
    
    if idade < 16:
        return idade, 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return idade, 'VOTO OPCIONAL'
    else:
        return idade, 'VOTO OBRIGATÓRIO'
    

while True:
    nasc = int(input('Digite o ano de nascimento: '))
    
    if nasc <= datetime.now().year and datetime.now().year - nasc < 200:
        break
    else:
        print('Ano Ínvalido, tente novamente! ')
        
idade, validacao = voto(nasc)

print(f'Com {idade} {'ano' if idade == 1 else 'anos'}: {validacao}')