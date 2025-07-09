'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python.
    só que fazendo a validação para aceitar apenas um valor númerico.
    Ex:
    n = leiaInt('Digite um n')'''

cores = {'limpa': '\033[m',
         'vermelho': '\33[31m'}

def leiaInt(txt):
    """
    -> Função que lê e valida a entrada de um número inteiro.
    :param txt: Texto (mensagem) exibido ao usuário.
    :return: Número inteiro validado.
    """
    
    while True:
        num = input(txt)
        if num.strip().lstrip('-').isdigit():
            return int(num)
        else:
            print(f'{cores["vermelho"]}ERRO! Digite um número inteiro válido!{cores["limpa"]}')
        

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')