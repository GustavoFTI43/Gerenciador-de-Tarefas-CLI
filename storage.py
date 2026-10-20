                # Ler arquivo
                # Salvar aquivo

from pathlib import Path
import json

arq_json = Path('Tarefas.json')

def carregar_arquivo():
    try:
        if not arq_json.exists():
            with open(arq_json, 'w' , encoding='utf-8') as arquivo:
                json.dump([] , arquivo)
        with open(arq_json, 'r' , encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError as e:
        print(f'{cor["Vermelho"]}Json Corrompido: {e}!{cor["Limpa"]}')
    else:
        try:
            if arq_json.exists():
                with open(arq_json , 'r' , encoding='utf-8') as arquivo:
                    return json.load(arquivo)
        except IOError as e:
            print(f'Erro ao abrir arquivo: {e}')


def salvar_arquivo(nova_tarefa):
    try:
        with open(arq_json, 'w', encoding='utf-8') as arquivo:
            json.dump(nova_tarefa, arquivo, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f'Erro ao abrir/escrever arquivo: {e}')
    except TypeError as e:
        print(f'Dado não pode ser convertido para JSON: {e}')


def titleFormat(msg , multind = 1):
    ind = (len(msg)+4) * multind
    print(f'{"-"* ind}\n{msg:^{ind}}\n{"-" * ind}')


def menu(lista):
    titleFormat('GERENCIADOR DE TAREFAS' , 3)

    for c , v in enumerate(lista):
        if c != 4:  # São 5 items
            print(f'{cor["Azul"]}[{c + 1}] {v}')
        else:
            print(f'[{c - 4}] {v}{cor["Limpa"]}')

def selectoption():
    while True:
        try:
            opcao = int(input(f'{cor["Azul"]}> Escolha uma opção: {cor["Limpa"]}'))
        except ValueError:
            print(f'{cor["Vermelho"]}Erro:  valor invalido tente novamente... {cor["Limpa"]}')
        except KeyboardInterrupt:
            print(f'\n{cor["Vermelho"]}Erro: Não foi digitado nenhum valor ... {cor["Limpa"]}')
            return 0
        else:
            if opcao not in range(0,5):
                print(f'{cor["Vermelho"]}Opção invalida! Tente novamente, Escolha entre 0 e 4 ...{cor["Limpa"]}')
            else:
                return opcao

# OBS; cores são aplicadas na exibição, não no armazenamento por isso criei as funções abaixo
# len_sem_cor e alinhar_celula removem os códigos ANSI
# para calcular o alinhamento correto da tabela
def len_sem_cor(txt):
    import re
    filtro = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return len(filtro.sub('' , str(txt)))

def alinhar_celula(txt,t):
    espacos_necessarios = t - len_sem_cor(txt)
    return str(txt) + (' ' * max(0, espacos_necessarios))

# era melhor aplicar cor apenas no print da função listar tarefa linha 47

cor = { 'Vermelho': '\033[31m' ,
'Verde': '\033[32m' ,
'Amarelo' : '\033[33m' ,
'Azul' : '\033[34m',
'Roxo' : '\033[35m',
'Limpa' : '\033[m'
}
