class ExemploContaBancarioPOO:
    def __init__(self, titular, numero, saldo_inicial = 0):
        self.titular = titular
        self.numero = numero
        self.saldo_inicial = saldo_inicial

        #depositar
    def depositar(self, valor):
        if valor>0:
            self.saldo_inicial = self.saldo_inicial + valor
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso")
        else:
            print("Valor invalido ")

    #sacar
    def sacar(self, valor):
        if valor<=0:
            print("Valor invalido ")
        elif valor>=self.saldo_inicial:
            print("Saldo invalido ")
        else:
            self.saldo_inicial = self.saldo_inicial - valor
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso")

    #fazer extrato
    def exibir_extrato(self):
        print("=" *20)
        print(f"Conta: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo_inicial:.2f}")
        print("="*20)

conta1 = ExemploContaBancarioPOO("Kaua", "0001", 1000000.00)
conta1.depositar(300000.00)
conta1.sacar(500000.00)
conta1.exibir_extrato()

conta2 = ExemploContaBancarioPOO("Gedian", "0002", 20.00)
conta2.depositar(5000.00)
conta2.exibir_extrato()

