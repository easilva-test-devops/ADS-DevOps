print('----- MENU PRINCIPAL -----\n')
print('(1) Gerenciar estudantes.')
print('(2) Gerenciar professores.')
print('(3) Gerenciar disciplinas.')
print('(4) Gerenciar turmas.')
print('(5) Gerenciar matrículas.')
print('(9) Sair.\n')
op = int(input('Informe a opção desejada: '))

if op == 1:
    print("\n\n***** [ESTUDANTES] MENU DE OPERAÇÕES *****\n")
elif op == 2:
    print("\n\n***** [PROFESSORES] MENU DE OPERAÇÕES *****\n")
elif op == 3:
    print("\n\n***** [DISCIPLINAS] MENU DE OPERAÇÕES*****\n")
elif op == 4:
    print("\n\n***** [TURMAS] MENU DE OPERAÇÕES *****\n")
elif op == 5:
    print("\n\n***** [MATRICULAS] MENU DE OPERAÇÕES *****\n")
elif op == 9:
    pass
else:
    print("\n\nOpção incorreta!")

print('(1) Incluir.')
print('(2) Listar.')
print('(3) Atualizar.')
print('(4) Excluir.')
print('(9) Voltar ao menu principal.\n')


