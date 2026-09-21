def validar_opcao_menu_principal(op: int) -> str:
    if op in [1, 2, 3, 4, 5]:
        modulos = {
            1: "ESTUDANTES",
            2: "PROFESSORES",
            3: "DISCIPLINAS",
            4: "TURMAS",
            5: "MATRICULAS"
        }
        return f"***** [{modulos[op]}] MENU DE OPERAÇÕES *****"
    elif op == 9:
        return "SAIR"
    else:
        return "Opção incorreta!"


def validar_acao_operacao(acao: int) -> str:
    acoes = {
        1: "INCLUSÃO",
        2: "LISTAGEM",
        3: "ATUALIZAÇÃO",
        4: "EXCLUSÃO"
    }
    if acao in acoes:
        return f"===== {acoes[acao]} ====="
    elif acao == 9:
        return "VOLTAR"
    else:
        return "Opção incorreta!"