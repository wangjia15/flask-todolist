import json
import os
from datetime import datetime
from typing import List, Dict, Any

class TodoManager:
    def __init__(self, data_file: str = "todos.json"):
        self.data_file = data_file
        self.ensure_data_file()

    def ensure_data_file(self):
        """确保数据文件存在"""
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def load_todos(self) -> List[Dict[str, Any]]:
        """从文件加载任务列表"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_todos(self, todos: List[Dict[str, Any]]):
        """保存任务列表到文件"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=2)

    def get_all_todos(self) -> List[Dict[str, Any]]:
        """获取所有任务"""
        return self.load_todos()

    def add_todo(self, title: str, description: str = "") -> Dict[str, Any]:
        """添加新任务"""
        todos = self.load_todos()
        new_todo = {
            "id": len(todos) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        todos.append(new_todo)
        self.save_todos(todos)
        return new_todo

    def update_todo(self, todo_id: int, **kwargs) -> Dict[str, Any]:
        """更新任务"""
        todos = self.load_todos()
        for todo in todos:
            if todo["id"] == todo_id:
                for key, value in kwargs.items():
                    if key in todo:
                        todo[key] = value
                if kwargs.get("completed") and not todo.get("completed_at"):
                    todo["completed_at"] = datetime.now().isoformat()
                self.save_todos(todos)
                return todo
        return None

    def delete_todo(self, todo_id: int) -> bool:
        """删除任务"""
        todos = self.load_todos()
        original_length = len(todos)
        todos = [todo for todo in todos if todo["id"] != todo_id]
        if len(todos) < original_length:
            self.save_todos(todos)
            return True
        return False

    def get_todo_by_id(self, todo_id: int) -> Dict[str, Any]:
        """根据ID获取任务"""
        todos = self.load_todos()
        for todo in todos:
            if todo["id"] == todo_id:
                return todo
        return None