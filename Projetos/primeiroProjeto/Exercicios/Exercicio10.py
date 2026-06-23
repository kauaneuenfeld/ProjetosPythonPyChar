usuario ="Admin"
senha = "Adim124"

tentativas = 5
while tentativas > 0:
    login = str(input("Digite o seu usuario: "))
    senha_digitada = str(input("Digite a sua senha: "))

    if login == usuario and senha_digitada == senha:
        print("Login realizado com sucesso!")
        break
    else:
        tentativas = tentativas - 1
        print("Usuario ou senha incorreto!")
        print(f"Você tem {tentativas} tentativas restantes.")

else:
    print("Você não tem mais tentativas, tente novamente mais tarde.")