agenda = {}

while True:
    print("\n1-Cadastrar")
    print("2-Consultar")
    print("3-Listar contatos")
    print("4-Filtrar por letra")
    print("5-Excluir contato")
    print("6-Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        if nome in agenda:
            print("Nome ja cadastrado")
        else:
            while True:
                telefone = input("Digite o telefone: ")
                if telefone != "":
                    break
                print("Telefone obrigatorio")

            agenda[nome] = telefone
            print("Cadastro realizado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome para buscar: ")
        if nome in agenda:
            print("Telefone: ", agenda[nome])
        else:
            print("Nome não encontrado")

    elif opcao == "3":
        if len(agenda) == 0:
            print("Agenda vazia")
        else:
            print("\nContatos cadastrados")
            contador = 1
            for nome, telefone in agenda.items():
                print(f"{contador} - {nome}: {telefone}")
                contador += 1

    elif opcao == "4":
        letra = input("Digite uma letra: ").upper()
        encontrou = False
        for nome, telefone in agenda.items():
            if nome.upper().startswith(letra):
                print(f"{nome} - {telefone}")
                encontrou = True
        if not encontrou:
            print("Nenhum contato encontrado")

    elif opcao == "5":
        nomeExcluir = input("Digite o nome do contato para excluir: ")
        if nomeExcluir in agenda:
            del agenda[nomeExcluir]
            print("Contato excluido")
        else:
            print("Contato nao encontrado")

    elif opcao == "6":
        break
