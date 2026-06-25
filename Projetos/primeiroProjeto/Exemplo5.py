agenda = {}

while True:
    print("\n1-Cadastrar")
    print("2-Consultar")
    print("3-Listar contatos")
    print("4-Sair")

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
            print("\nLista de contatos")
            contador = 1
            for nome, telefone in agenda.items():
                print(f"{contador} - {nome}: {telefone}")
                contador += 1

    elif opcao == "4":
        break
