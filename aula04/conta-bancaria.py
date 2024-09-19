class Conta:

    def __init__(self, pessoa, tipo, numero, saldo):
        self.pessoa=pessoa
        self.tipo=tipo
        self.numero=numero
        self.saldo=saldo

    def listar(self):
        print('###################')
        print(f'\nDono da conta: {self.pessoa}')
        print(f'Tipo: {self.tipo}')
        print(f'Número da conta: {self.numero}')
        print(f'Saldo: {self.saldo}\n')
        print('###################')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

def entrada():
    pessoa=input('Digite nome do cliente: ')
    tipo=input('Digite sua modalidade de conta: [Corrente/Poupança] ')
    numero=input('Digite o número da conta: ')
    saldo=float(input('Digite o saldo inicial: R$ '))
    return(pessoa, tipo, numero, saldo)


if __name__ == '__main__':
    # conta_Lisiane = Conta()
    # conta_Lisiane.pessoa = 'Lisiane'
    # conta_Lisiane.tipo = 'Corrente'
    # conta_Lisiane.numero = '1234-5'
    # conta_Lisiane.saldo = 503.45
    # conta_Lisiane.listar()
    #
    # conta_Henrique = Conta()
    # conta_Henrique.pessoa = 'Henrique'
    # conta_Henrique.tipo = 'Poupança'
    # conta_Henrique.numero = '2245-4'
    # conta_Henrique.saldo = 1008.38
    # conta_Henrique.listar()
    #
    # conta_Artur = Conta()
    # conta_Artur.pessoa = 'Artur'
    # conta_Artur.tipo =  'Corrente'
    # conta_Artur.numero = '1342-5'
    # conta_Artur.saldo = 932.27
    # conta_Artur.listar()

    pessoa, tipo, numero, saldo = entrada()
    conta_Pessoa=Conta(pessoa, tipo, numero, saldo)
    conta_Pessoa.listar()
    conta_Pessoa.listar()
