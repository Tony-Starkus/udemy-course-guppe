"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

OBS: O MÓDULO PICKLE NÃO É SEGURO CONTRA DADOS MALICIOSOS, POR ISSO, NÃO É RECOMENDADO TRABALHAR COM ARQUIVOS PICKLE
VINDOS DE PESSOAS/FONTES DESCONHECIDAS.


# Serializando no pickle
felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open("animais.pickle", "wb") as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""
import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f"{self.__nome} está comendo")


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f"{self._Animal__nome} está miando...")


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f"{self._Animal__nome} está latindo...")


# Deserializando o pickle
with open("animais.pickle", "rb") as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f"O gato se chama {gato._Animal__nome}")
