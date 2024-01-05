from db import *
from functions import *

def ln(x):
    print("-"*x)

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
            print("Chamar a função para o item correspondente")
        case 2:
            print("Chamar a função para o item correspondente")
        case 3:
            print("Concluídas...")
        case 4:
            print("Categorias...")
        case 5:
            print("Prioridades...")
        case 0:
            print("Saindo...")
            break
        



