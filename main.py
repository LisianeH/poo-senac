
from animal import Animal
from cachorro import Cachorro
from gato import Gato
from passaro import Passaro


if __name__ == '__main__':
    cachorro1 = Cachorro("Rex", 3, "Labrador")
    gato1 = Gato("Mia", 2, "Branca")
    passaro1 = Passaro("Piu-Piu", 1, "Canario")

    cachorro1.emitir_som()
    gato1.emitir_som()
    passaro1.emitir_som()
