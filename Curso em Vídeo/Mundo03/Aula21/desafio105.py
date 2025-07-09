'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos 
    e vai retornar um dicionário com as  seguintes informações:
        - Quantidade de notas;
        - A maior nota;
        - A menor nota;
        - A média da turma;
        - A situação (opcional);
    Adicione também as docstrings da função.'''

def notas(*nt, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nt: uma ou mais notas dos alunos (aceita múltiplos valores).
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com informações sobre as notas e, opcionalmente, a situação da turma.
    """

    boletim = {}
    boletim['total'] = len(nt)
    boletim['maior'] = max(nt)
    boletim['menor'] = min(nt)
    boletim['media'] = round((sum(nt)/len(nt)), 2)
    
    if situacao:
        if boletim['media'] >= 7:
            boletim['situação'] = 'BOA'
        elif boletim['media'] >= 6:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'
        
    return boletim
    

resp = notas(3.5, 2, 6.5)
help(notas)