def realizar_login(usuario, senha, forcar_erro):
    resultado_login = False
    senha = "123456"
    if usuario and senha is True:
        print("Usuário Válidado.")
    else:
        print("Usuário e/ou Senha Inválidos, tente novamente.")

    if forcar_erro is False:
        print("Iniciando o processo de login no sistema com credenciais válidas... ")
        print("Aguardando o tempo de resposta do servidor...")
        resultado_login = True
    else:
        print("Erro forçado.")
    return resultado_login


def test_verificar_login_valido():
    token_sessao = "abc123xyz"
    resultado = realizar_login(True, "123456", False)
    assert resultado is True
    if resultado is True:
        print(f"Login efetuado com sucesso! Entre na sessão: {token_sessao}")
    else:
        print("Login Inválido, tente novamente.")
