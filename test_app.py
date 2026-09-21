from app import validar_opcao_menu_principal, validar_acao_operacao


def test_menu_principal_estudantes():
    resultado = validar_opcao_menu_principal(1)
    assert resultado == "***** [ESTUDANTES] MENU DE OPERAÇÕES *****"


def test_menu_principal_opcao_invalida():
    resultado = validar_opcao_menu_principal(99)
    assert resultado == "Opção incorreta!"


def test_menu_principal_sair():
    resultado = validar_opcao_menu_principal(9)
    assert resultado == "SAIR"


def test_acao_operacao_inclusao():
    resultado = validar_acao_operacao(1)
    assert resultado == "===== INCLUSÃO ====="


def test_acao_operacao_opcao_invalida():
    resultado = validar_acao_operacao(7)
    assert resultado == "Opção incorreta!"