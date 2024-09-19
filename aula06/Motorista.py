import random

class Motorista:
    def __init__(self, nome, idade, cnh, caminhao):
        self.nome = nome
        self.idade = idade
        self.cnh = cnh
        self.caminhao = caminhao

    def identificar(self, nome, idade, cnh, caminhao):
        self.nome = input("Digite o nome do motorista: ")
        self.idade = int(input("Qual ano de nascimento de " + nome + " : "))
        self.cnh = input("Digite a CNH (número de registro): ")
        self.caminhao = None

    def gerar_id(self):
        return random.randint(1000, 2000)
