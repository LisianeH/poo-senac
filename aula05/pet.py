from idlelib.mainmenu import menudefs
import random as rm

## Class Animal
class AnimalEstimacao:

    def __init__(self, nome, especie, idade, tutor):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.estado = None
        self.tutor = tutor

    def comer(self):
        comendo = ["Comendo"]
        self.estado = rm.choice(comendo)

    def dormir(self):
        dormindo = ["Dormindo"]
        self.estado = rm.choice(dormindo)

    def brincar(self):
        brincando = ["Brincando"]
        self.estado = rm.choice(brincando)

    def random(self):
        acoes = [self.comer, self.dormir, self.brincar]
        acao_escolhida = rm.choice(acoes)
        acao_escolhida()

    def comentar(self):
        print('*****')
        print(f'\nO {self.nome} é um {self.especie} que tem {self.idade} anos e está {self.estado} neste momento')
        print(f'Seu tutor é {self.tutor.nome} {self.tutor.celular}')
        print('*****')

## Class Tutor
class Tutor:

    def __init__(self, nome, cpf, celular):
        self.nome = nome
        self.cpf = cpf
        self.celular = celular

    def listar(self):
        print('\n')
        print(f'''
            Lista Tutor
            Nome: {self.nome}  
            CPF: {self.cpf}
            Celular: {self.celular}
        ''')

def entradaTutor():
    nome = input("Digite seu nome (Tutor): ")
    cpf = input(f"Digite seu CPF: ")
    celular = input(f"Digite seu celular (com DDD): ")
    return nome, cpf, celular

def entradaPet():
    nome = input("Digite o nome do seu pet: ")
    especie = input(f"Digite a espécie de {nome}: ")
    idade = input(f"Digite a idade de {nome}: ")
    return nome, especie, idade

if __name__ == '__main__':
    nome, especie, idade = entradaPet()
    nomeTutor, cpf, celular = entradaTutor()
    tutor1 = Tutor(nomeTutor, cpf, celular)
    pet1 = AnimalEstimacao(nome, especie, idade, tutor1)
    pet1.random()
    pet1.comentar()

