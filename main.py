from db import *
from functions import *
from datetime import datetime

# projetosfortal@infinityschool.com.br

# INÍCIO FUNÇÕES DO PY TASK -------------------------------------

def ln(x):
    print("-"*x)

def add_task():
    id = len(db_tarefas),
    descricao = input("Digite a descrição da tarefa: ")
    categoria = input("Digite a categoria da tarefa: ")
    prioridade = int(input("Defina a prioridade - de 0 a 3: "))
    

    dic_task = {
        "ID": id,
        "Descrição": descricao,
        "Categoria": categoria,
        "Prioridade": prioridade,
        "Concluido": False
    }

    db_tarefas.append(dic_task)


def list_tasks():
    ln(30)
    for i, item in enumerate(db_tarefas):
        print(f"""
        {i+1}ª
        Prioridade: {item['Prioridade']}
        Descrição: {item['Descrição']}
        Categoria: {item['Categoria']}
        Status: {item['Concluido']}
        """)

def alter_task():
    index_task = int(input("Deseja concluir qual tarefa?\n"))
    db_tarefas[index_task]['Concluido'] = not db_tarefas[index_task]['Concluido']
    list_tasks()


# FIM FUNÇÕES DO PY TASK ----------------------------------------

print("Sistema Py Task")
ln(30)

while True:
    menu = int(input("""Escolha uma opção:
            1 - Adicionar Tarefa
            2 - Listar tarefas
            3 - Marcar como concluído
            4 - Exibir tarefas por categoria
            5 - Exibir tarefas por prioridade
            0 - Sair
            """))
    match menu:
        case 1:
            add_task()
        case 2:
            list_tasks()
        case 3:
            alter_task()
        case 4:
            print("Homens trabalhando...")
        case 5:
            print("Homens trabalhando...")
        case 0:
            print("Saindo...")
            break
        
