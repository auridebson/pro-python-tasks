tarefa = { }

db_tarefas = [
    {
        'ID': '2024, 1, 5, 10, 28, 10, 783891', 
        'Descrição': 'Banhar os cachorros', 
        'Categoria': 'Casa', 
        'Prioridade': 0, 
        'Concluido': False
    },
    {
        'ID': '2024, 1, 5, 10, 28, 24, 969222', 
        'Descrição': 'Comprar frutas para casa', 
        'Categoria': 'Casa', 
        'Prioridade': 2, 
        'Concluido': False
    },
    {
        'ID': '2024, 1, 5, 10, 28, 24, 969222', 
        'Descrição':'Estudar JavaScript',
        'Categoria': 'Estudos', 
        'Prioridade': 1, 
        'Concluido': False
    }
]

def list_tasks():
    for i, item in enumerate(db_tarefas):
        print(f"""
        {i+1}ª
        Prioridade: {item['Prioridade']}
        Descrição: {item['Descrição']}
        Categoria: {item['Categoria']}
        """)


def alter_task():
    index_task = int(input("Deseja concluir qual tarefa? "))
    db_tarefas[index_task]['Concluido'] = True
    print(db_tarefas[index_task])


alter_task()