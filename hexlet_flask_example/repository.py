import os
import json


class UsersRepository:
    def __init__(self):
        self.user_db = os.path.join(
            os.path.dirname(__file__), 'templates', 'users', 'user_db'
        )

    def save(self, data):
        # Проверяем, существует ли файл
        if not os.path.exists(self.user_db):
            with open(self.user_db, 'w') as repo:
                json.dump([], repo)  # Создаём файл с пустым списком

        # Читаем существующие данные
        with open(self.user_db, 'r') as repo:
            try:
                repo_list = json.load(repo)
            except json.JSONDecodeError:
                repo_list = []  # В случае ошибки декодирования JSON присваиваем пустой список

        # Добавляем новые данные и записываем обратно
        repo_list.append(data)
        with open(self.user_db, 'w') as repo:
            json.dump(repo_list, repo)

    def content(self):
        with open(self.user_db, 'r') as repo:
            result = json.loads(repo.read())
            return result

    def find(self, id):
        items = self.content()
        for item in items:
            if str(item['id']) == id:
                return item
