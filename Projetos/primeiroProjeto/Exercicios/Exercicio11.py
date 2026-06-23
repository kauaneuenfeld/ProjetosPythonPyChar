import random

tentativas = 5

numero = random.randint(1, 100)

while tentativas > 0:
    chute = int(input("Digite um numero de 1 a 100: "))

    if chute < numero:
        print("O numero é maior que seu palpite")
        tentativas = tentativas - 1
        print(f"Voce tem {tentativas} tentativas")

    elif chute > numero:
        print("O numero é menor que seu palpite")
        tentativas = tentativas - 1
        print(f"Voce tem {tentativas} tentativas")

    else:
        print("Vc acertou")

else:
    print("Voce nao acertou")
    print(f"o numero era {numero}")


