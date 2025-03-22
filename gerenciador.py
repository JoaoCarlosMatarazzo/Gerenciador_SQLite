import requests
import json

# URL do banco de dados Firebase Realtime (substitua pela URL do seu projeto Firebase)
FIREBASE_URL = "https://seu-projeto.firebaseio.com/tasks.json"

# Função para adicionar uma nova tarefa ao banco de dados
def add_task(title, description=""):
    task_data = {
        "title": title,
        "description": description,
        "completed": False
    }
    response = requests.post(FIREBASE_URL, json=task_data)
    if response.status_code == 200:
        print("Tarefa adicionada!")
    else:
        print("Erro ao adicionar tarefa")

# Função para listar todas as tarefas armazenadas no banco de dados
def list_tasks():
    response = requests.get(FIREBASE_URL)
    if response.status_code == 200 and response.json():
        tasks = response.json()
        for task_id, task in tasks.items():
            status = "✔" if task["completed"] else "✘"
            print(f"[{status}] {task_id} - {task['title']}: {task['description']}")
    else:
        print("Nenhuma tarefa encontrada.")

# Função para marcar uma tarefa como concluída
def complete_task(task_id):
    task_url = f"https://seu-projeto.firebaseio.com/tasks/{task_id}.json"
    response = requests.patch(task_url, json={"completed": True})
    if response.status_code == 200:
        print("Tarefa concluída!")
    else:
        print("Erro ao concluir tarefa")

# Função para excluir uma tarefa do banco de dados
def delete_task(task_id):
    task_url = f"https://seu-projeto.firebaseio.com/tasks/{task_id}.json"
    response = requests.delete(task_url)
    if response.status_code == 200:
        print("Tarefa excluída!")
    else:
        print("Erro ao excluir tarefa")

# Função para buscar tarefas com base em uma palavra-chave
def search_tasks(keyword):
    response = requests.get(FIREBASE_URL)
    if response.status_code == 200 and response.json():
        tasks = response.json()
        for task_id, task in tasks.items():
            if keyword.lower() in task["title"].lower() or keyword.lower() in task["description"].lower():
                status = "✔" if task["completed"] else "✘"
                print(f"[{status}] {task_id} - {task['title']}: {task['description']}")
    else:
        print("Nenhuma tarefa encontrada.")

# Bloco principal do código para interagir com o usuário
task = input("Digite o nome da nova tarefa: ")
description = input("Digite uma descrição (opcional): ")
add_task(task, description)
list_tasks()
