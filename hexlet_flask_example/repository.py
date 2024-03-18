import os


class UsersRepository:
    def __init__(self):
        self.user_db = os.path.join(
            os.path.dirname(__file__), 'templates', 'users', 'user_db'
        )

    def data_write(self, data):
        with open(self.user_db, 'a') as repo:
            repo.write(data)

    def data_read(self, data):
        with open(self.user_db, 'r') as repo:
            result = repo.read(data)
            return result
