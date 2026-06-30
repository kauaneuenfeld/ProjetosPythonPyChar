class Produto:
    total_cadastrado = 0
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

        Produto.total_cadastrado += 1

    def valor_em_estoque(self):
        return self.preco * self.quantidade

    def aplicar_desconto(self, percentual):
        if 0 < percentual < 100:
            self.preco -= self.preco * (percentual/100)
        else:
            print("Persentual de desconto invalido")

    def info(self):
        print(f"Produto: {self.nome}")
        print(f"PPreço: {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Total: {self.valor_em_estoque():.2f}")

    @classmethod
    def  exibir_cadastro(cls):
        print(f"Total de produtos cadastrados: {cls.total_cadastrado}")

p1 = Produto("Notebook", 3500, 10)
p2 = Produto("Mouse", 89.90, 50)

p1.info()

print("\n")

p2.aplicar_desconto(10)
p2.info()

Produto.exibir_cadastro()

