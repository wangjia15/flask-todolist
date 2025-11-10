from flask import Flask, render_template, request, jsonify, redirect, url_for
from todo_manager import TodoManager

app = Flask(__name__)
todo_manager = TodoManager()

@app.route('/')
def index():
    """首页 - 显示所有任务"""
    todos = todo_manager.get_all_todos()
    return render_template('index.html', todos=todos)

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """获取所有任务 API"""
    todos = todo_manager.get_all_todos()
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    """添加新任务 API"""
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    title = data['title'].strip()
    description = data.get('description', '').strip()

    if not title:
        return jsonify({'error': 'Title cannot be empty'}), 400

    new_todo = todo_manager.add_todo(title, description)
    return jsonify(new_todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """更新任务 API"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    updated_todo = todo_manager.update_todo(todo_id, **data)
    if updated_todo:
        return jsonify(updated_todo)
    return jsonify({'error': 'Todo not found'}), 404

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """删除任务 API"""
    if todo_manager.delete_todo(todo_id):
        return jsonify({'message': 'Todo deleted successfully'})
    return jsonify({'error': 'Todo not found'}), 404

@app.route('/api/todos/<int:todo_id>/toggle', methods=['POST'])
def toggle_todo(todo_id):
    """切换任务完成状态 API"""
    todo = todo_manager.get_todo_by_id(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404

    updated_todo = todo_manager.update_todo(todo_id, completed=not todo['completed'])
    return jsonify(updated_todo)

if __name__ == '__main__':
    app.run(debug=True)