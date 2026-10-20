                # menu principal
                # importe os modulos e bibliotecas necessarias
from time import sleep
from storage import *
from tarefas import *





while True:
    menu(['Adicionar Tarefa','Listar Tarefas','Concluir Tarefa','Deletar Tarefa','Sair'])
    resp = selectoption()
                # adicione uma nova tafera se resp == 1
    if resp == 1:
        adicionar()
        sleep(2)
                # listar tarefas
    elif resp == 2:
        listar_tarefa()
        sleep(2)
    elif resp == 3:
        concluir_tarefa()
        sleep(2)
    elif resp == 4:
        deletar_tarefa()
        sleep(2)
    else:
        print('Encerrando Programa ...')
        sleep(1)
        print('                             Até logo ...')
        break
