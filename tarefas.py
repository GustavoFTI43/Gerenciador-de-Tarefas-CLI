                # logica do programa
                # adicionar nova tarefa:
from storage import *
from datetime import date
def adicionar():
    while True:
        try:
            discricao = dict()
            data = date.today()
            name_tarefa = str(input(f'{cor["Azul"]}descreva a tarefa que quer adicionar: {cor["Limpa"]}')).title().strip()
            if name_tarefa.replace(' ', '').isalpha():
                discricao['discrição'] = name_tarefa
            else:
                print(f'{cor["Vermelho"]}Erro: Tente novamente ...{cor["Limpa"]}')
                continue
            prioridade = str(input(f'{cor["Azul"]}Qual Prioridade da Tarefa [Alta] ou [Baixa] : {cor["Limpa"]}')).title().strip()[:1]
            if prioridade in 'Ba' and prioridade.replace(' ','').isalpha():
                discricao['Prioridade'] = f'{cor["Roxo"]}Baixa{cor["Limpa"]}'

            elif prioridade in 'Al'and prioridade.replace(' ','').isalpha():
                discricao['Prioridade'] = f'{cor["Vermelho"]}Alta{cor["Limpa"]}'
            else :
                print(f'{cor["Vermelho"]}Erro. Tente novamnete e Digite a Prioridade da Tarefa !!! {cor["Limpa"]}')
                continue
        except KeyboardInterrupt:
            print(f'{cor["Vermelho"]}\nErro: não foi digitado nada ... {cor["Limpa"]}')
            break

        else:
            discricao['status'] = 'pendente'
            discricao['data_criada'] = f'{data.day}/{data.month}/{data.year}'
            arquivo = carregar_arquivo()
            arquivo.append(discricao)
            salvar_arquivo(arquivo)
            print(f'{cor["Verde"]}             Nova tarefa adicionada com sucesso!{cor["Limpa"]}\n')
            break


def listar_tarefa():
    dados = carregar_arquivo()
    if len(dados) == 0:
        return print(f'{cor["Amarelo"]}Ainda não a tarefas em sua LISTA DE TAREFAS.{cor["Limpa"]}')
    else:
        titleFormat('LISTA DE TAREFAS' , 4)
        print(f'{cor["Amarelo"]}{"Tarefa." :<25}{"Prioridade.":<20}{"Status.":<20}{"Data.":<15}{cor["Limpa"]}')
        for d in dados:
            print(f'{d["discrição"] :<25}{alinhar_celula(d["Prioridade"] , 20)}{alinhar_celula(d["status"] , 20)}{d["data_criada"]:<15}')
        print('-' * 80)




def concluir_tarefa():
    while True:
        arquivo = carregar_arquivo()
        try:
            if len(arquivo) == 0:
                print(f'{cor["Amarelo"]}Não a tarefas a serem concluidas , adicione uma tarefas primeiro !!!{cor["Limpa"]}')
                break
            else:
                opção = int(input(f'{cor["Azul"]}Digite a tarefa que quer concluir ou [0] para voltar ao menu: {cor["Limpa"]}'))
        except ValueError:
            print(f'{cor["Vermelho"]}Erro: Digite um valor valido ...{cor["Limpa"]}')
            continue
        except KeyboardInterrupt:
            print(f'{cor["Vermelho"]}\nErro: não foi digitado nada ... {cor["Limpa"]}')
            break
        else:
            if opção == 0:
                print('Voltando ao menu inicial ...')
                break
            if opção > len(arquivo):
                print(f'{cor["Vermelho"]}Erro. numero de tarefa invalida, para ver as tarefas pendentes aperte [0] para voltar ao menu!!!{cor["Limpa"]}')
            else:
                arquivo[opção-1]['status'] = f'{cor["Verde"]}concluido{cor["Limpa"]}'
                salvar_arquivo(arquivo)
                print(f'\n{cor["Verde"]}         Tarefa concluida com sucesso !{cor["Limpa"]}\n')
                break

def deletar_tarefa():
    arquivo = carregar_arquivo()
    while True:
        try:
            if len(arquivo) == 0 :
                print(f'{cor["Amarelo"]}Não a tarefas a serem excluidas , adicione uma tarefas primeiro !!!{cor["Limpa"]}')
                break
            else:
                opção = int(input(f'{cor["Azul"]}Digite a tarefa que quer deletar ou [0] para voltar ao menu: {cor["Limpa"]}'))
        except ValueError:
            print(f'{cor["Vermelho"]}Erro: Digite um valor valido ...{cor["Limpa"]}')
            continue
        except KeyboardInterrupt:
            print(f'{cor["Vermelho"]}\nErro: não foi digitado nada ... {cor["Limpa"]}')
            break
        else:
            if opção == 0:
                print('Voltando ao menu inicial ...')
                break
            if opção > len(arquivo):
                print(f'{cor["Vermelho"]}Erro. numero de tarefa invalida, para ver as tarefas pendentes aperte [0] para voltar ao menu!!!{cor["Limpa"]}')
            else:
                del arquivo[opção-1]
                salvar_arquivo(arquivo)
                print(f'\n{cor["Verde"]}         Tarefa deletada com sucesso !{cor["Limpa"]}\n')
                break


