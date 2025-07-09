'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
    Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
    OBS: use cores.'''
    
from time import sleep

cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'branco': '\033[1;40m',
         'azul': '\033[1;34m',
         'ciano': '\033[1;36m'}

def ajuda(cmnd='', cor='limpo'):
    """
    -> Função para exibir o help formatado.
    :param cmnd: Comando inserido na função help().
    :param cor: Cor para o texto.
    :return: Exibe o help formatado no terminal.
    """
    ajustarTxt(f"Acessando o manual do comando '{cmnd}'", 'azul')
    
    sleep(1.5)
    print(formatar(cor))
    help(cmnd)
    print(formatar('limpo'))
    sleep(2)
    
    
def formatar(cor='limpo'):
    """
    -> Função para aplicar cor ao texto no terminal.
    :param cor: Nome da cor definida no dicionário 'cores'.
    :return: Imprime o código ANSI da cor.
    """
    
    print(cores[cor])


def ajustarTxt(txt, cor='limpo'):
    """
    -> Função para exibir um texto centralizado com borda e cor.
    :param txt: Texto a ser exibido.
    :param cor: Cor opcional aplicada ao texto (definida em 'cores').
    :return: Imprime o texto decorado no terminal.
    """

    tamn = len(txt) + 4
    
    print(cores[cor] + '~'*tamn)
    print(f'{txt:^{tamn}}')
    print('~'*tamn + cores['limpo'])


while True:

    ajustarTxt('SISTEMA DE AJUDA PyHELP', 'verde')
    sleep(1.5)
    
    formatar('ciano')
    texto = str(input('Função ou Biblioteca > ')).strip().lower()
    formatar('limpo')
    
    if texto == 'fim':
        ajustarTxt('ATÉ LOGO !', 'vermelho')
        sleep(1.5)
        break
    else:
        ajuda(texto, 'branco') 