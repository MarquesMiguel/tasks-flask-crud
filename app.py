# nome do arquivo precisar ser app
from flask import Flask, request, jsonify
from models.task import Task

# quando executamos esse arquivo diretamente __name__ = "__main__"
app = Flask(__name__) # utilizamos a classe Flask para criar o objeto app __name__ = nome do nosso aplicativo

# Rota: comunicar com outros clientes receber e devolver info
#CRYD 
#Create, Read, Update and Delete = CRUD
#tabela: tarefa


tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control #acessar a variavel task_id_control 
    data = request.get_json()
    new_task = Task(id=task_id_control,title=data["title"], description=data.get("description", "")) #string vazia caso o cliente nao envie
    task_id_control += 1
    tasks.append(new_task)
    print(data)
    print(tasks)
    return jsonify({"message": "nova tarefa criada com sucesso", "id": new_task.id})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    # for task in tasks:
    #     task_list.append(task.to_dict())
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])  # parametro de rota, permite que receba uma informação do cliente na rota (converte p int)
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso", }), 200

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        print(t.to_dict())
        if t.id == id:
            task = t
            break   # pois continuaria percorrendo mesmo apos achar
    
    if not task:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

# modo debug somente se o arquivo for executado de forma manual
if __name__ == "__main__":
    app.run(debug=True)
