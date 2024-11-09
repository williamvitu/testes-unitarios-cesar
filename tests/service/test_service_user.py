

from src.service.service_user   import ServiceUser
from src.models.user            import User


class TestServiceUser():

    def test_add_user_success(self):

        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario adicionado"

        # Chamada
        resultado = service.add_user("Vitor", "Analista")

        # Validação
        assert resultado == resultado_esperado

    def test_add_user_type_error(self):

        # Setup
        service = ServiceUser()
        resultado_esperado = "Type error"
        service.add_user("Vitor", "Analista")

        # Chamada
        resultado = service.add_user("Vitor", 50)

        # Validação
        assert resultado == resultado_esperado

    def test_add_user_already_exist(self):

        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = "Usuario já existe"

        # Chamada
        resultado =  service.add_user("Vitor", "Analista")

        # Validação
        assert resultado == resultado_esperado


    def test_add_user_empty_name(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Var is empty"

        # Chamada
        resultado = service.add_user(None, "Analista")

        # Validação
        assert resultado == resultado_esperado

    def test_remove_user_success(self):
        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = "Usuario removido"

        # Chamada
        resultado = service.remove_user("Vitor")

        # Validação
        assert resultado == resultado_esperado

    def test_remove_user_type_error(self):
        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = "Type error"

        # Chamada
        resultado = service.remove_user([])

        # Validação
        assert resultado == resultado_esperado

    def test_remove_user_empty_parameter(self):
        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = "Var is empty"

        # Chamada
        resultado = service.remove_user(None)

        # Validação
        assert resultado == resultado_esperado

    def test_remove_user_non_existing_user(self):
        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = "Usuario não existe"

        # Chamada
        resultado = service.remove_user("HAHAHAHAHA")

        # Validação
        assert resultado == resultado_esperado

    def test_update_user_success(self):
        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = "Trabalho atualizado para Desenvolvedor"

        # Chamada
        resultado = service.update_user("Vitor", "Desenvolvedor")

        # Validação
        assert resultado == resultado_esperado

    def test_update_user_type_error(self):
        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = "Type error"

        # Chamada
        resultado = service.update_user("Vitor", [])

        # Validação
        assert resultado == resultado_esperado

    def test_update_user_empty_parameter(self):
        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = "Var is empty"

        # Chamada
        resultado = service.update_user(None, "Teste")

        # Validação
        assert resultado == resultado_esperado


    def test_get_user_success(self):
        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = ("Vitor", "Analista")

        # Chamada
        user = service.get_user_by_name("Vitor")
        resultado = (user.name, user.job)

        # Validação
        assert type(user) == User
        assert resultado == resultado_esperado

    def test_get_user_parameter_empty(self):
        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = "Var is empty"

        # Chamada
        resultado = service.get_user_by_name(None)


        # Validação
        assert resultado == resultado_esperado

    def test_get_user_type_error(self):
        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = "Type error"

        # Chamada
        resultado = service.get_user_by_name([])


        # Validação
        assert resultado == resultado_esperado

    def test_get_user_not_exist_in_db(self):
        # Setup
        service = ServiceUser()
        service.add_user("Vitor", "Analista")
        resultado_esperado = "Usuario não existe no banco"

        # Chamada
        resultado = service.get_user_by_name("Gildo")


        # Validação
        assert resultado == resultado_esperado