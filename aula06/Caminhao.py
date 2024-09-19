
class Caminhao:
    def __init__(self, modelo, placa, capacidade, motorista):
        self.modelo = modelo
        self.placa = placa
        self.capacidade = capacidade
        self.motorista = motorista

def identificar():
    modelo = input("Digite o modelo do caminhão: ")
    placa = input("Qual a placa? ")
    capacidade = input("Qual a capacidade de carga? ")
    motorista = int(input("Digite o ID: "))
