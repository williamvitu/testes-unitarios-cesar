from src.models.store import  Store
from src.models.user  import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):

        if name is not None and job is not None:

            if type(name) != str or type(job) != str:
                return "Type error"

            user = User(name, job)

            for db_user in self.store.bd:
                if user.name == db_user.name:
                    return "Usuario já existe"

            self.store.bd.append(user)
            return "Usuario adicionado"

        return "Var is empty"

    def remove_user(self, name):
        if name is not None:
            if type(name) != str:
                return "Type error"

            for db_user in self.store.bd:
                if name == db_user.name:
                    self.store.bd.remove(db_user)
                    return "Usuario removido"

            return "Usuario não existe"

        return "Var is empty"


    def update_user(self, name, job):

        if name is not None:

            if type(name) != str or type(job) != str:
                return "Type error"

            user = self.get_user_by_name(name)

            if type(user) == User:
                user.job = job
                return f"Trabalho atualizado para {user.job}"

            return user
        return "Var is empty"

    def get_user_by_name(self, name):

        if name is not None:
            if type(name) != str:
                return "Type error"

            for db_user in self.store.bd:
                if name == db_user.name:
                    return db_user

            return "Usuario não existe no banco"

        return "Var is empty"