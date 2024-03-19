import os
import json


class UsersRepository:
    def __init__(self):
        self.user_db = os.path.join(
            os.path.dirname(__file__), 'templates', 'users', 'user_db'
        )

    def data_write(self, data):
        with open(self.user_db, 'a') as repo:
            repo.write(json.dumps(data))

    def content(self):
        with open(self.user_db, 'r') as repo:
            result = json.loads(repo.read())
            return result

    def find(self, id):
        items = self.content()
        for item in items:
            if str(item['id']) == id:
                return item
