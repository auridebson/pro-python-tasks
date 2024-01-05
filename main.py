from db import *
from functions import *
from datetime import datetime

# INÍCIO FUNÇÕES DO PY TASK -------------------------------------

def ln(x):
    print("-"*x)

def add_task():
    timestamp = str(datetime.now()),
    descricao = input("Digite a descrição da tarefa: ")
    categoria = input("Digite a categoria da tarefa: ")
    prioridade = int(input("Defina a prioridade - de 0 a 3: ")),
    

    dic_task = {
        "ID": timestamp,
        "Descrição": descricao,
        "Categoria": categoria,
        "Prioridade": prioridade,
        "Concluido": False
    }

    db_tarefas.append(dic_task)


def list_tasks():
    for item in db_tarefas:
        print(f"""
           Descrição: {item['descricao']}
           Categoria: {item['categoria']}
           Prioridade: {item['prioridade']}
           Concluido: {item['concluido']}
        """)

# FIM FUNÇÕES DO PY TASK -------------------------------------

print("Sistema Py Task")
ln(30)

while True:
    menu = int(input("""Escolha uma opção:
            1 - Adicionar Tarefa
            2 - Listar tarefas
            3 - Marcar como concluído
            4 - Exibir tarefas por categoria
            5 - Exibir taregas por prioridade
            0 - Sair
            """))
    match menu:
        case 1:
            add_task()
        case 2:
            list_tasks()
        case 3:
            print("Concluídas...")
        case 4:
            print("Categorias...")
        case 5:
            print("Prioridades...")
        case 0:
            print("Saindo...")
            break
        



