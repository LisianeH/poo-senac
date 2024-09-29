#Lisiane Hoffmeister

class Produto:
    # construtor
    def __init__(self, codigo, nome, categoria, preco, quantidadeEstoque, quantidadeVendida=0):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidadeEstoque = quantidadeEstoque
        self.quantidadeVendida = quantidadeVendida

    # funções de get
    def get_codigo(self):
        return self.codigo

    def get_nome(self):
        return self.nome

    def get_categoria(self):
        return self.categoria

    def get_preco(self):
        return self.preco

    def get_quantidadeEstoque(self):
        return self.quantidadeEstoque

    # Cálculo para calcular quantidade vendida e valor da compra
    def vender(self, quantidadeVendida):
        if quantidadeVendida <= self.quantidadeEstoque:
            self.quantidadeEstoque -= quantidadeVendida
            self.quantidadeVendida += quantidadeVendida  # Atualizando a quantidade vendida
            totalCusto = quantidadeVendida * self.preco
            print(f"\nVenda realizada com sucesso! "
                  f"\n{quantidadeVendida} unidades de {self.nome} vendidas por R$ {totalCusto:.2f}.")
        else:
            print("Estoque insuficiente para realizar a venda.")

    # Cálculo para adicionar estoque de produto
    def adicionar(self, quantidadeAdquirida):
        self.quantidadeEstoque += quantidadeAdquirida
        print(f"\nAdicionado ao estoque de {self.nome}, {quantidadeAdquirida} unidades, "
              f"atualizando a quantidade de estoque para {self.quantidadeEstoque} unidades")

    def listar(self):
        totalCusto = self.quantidadeVendida * self.preco
        return (
            "\n**********"
            f"\nNome: {self.nome}"
            f"\nCategoria: {self.categoria}"
            f"\nQuantidade Vendida: {self.quantidadeVendida}"
            f"\nPreço: R${self.preco:.2f}"
            f"\nTotal das Vendas: R$ {totalCusto:.2f}"
            f"\nTotal no estoque: {self.quantidadeEstoque}"
            "\n**********"
        )

# TESTANDO O PROGRAMA
produto1 = Produto(1, "Camisa", "Vestuário", 79.90, 75)
# Imprimindo somente nome do produto1
print(produto1.get_nome())
# Utilizando o metodo vender com 1 unidade vendida
produto1.vender(5)
# Utilizando o metodo adicionar com 10 unidades de camisas adquiridas
produto1.adicionar(10)
# Listando as informações do produto
print(produto1.listar())