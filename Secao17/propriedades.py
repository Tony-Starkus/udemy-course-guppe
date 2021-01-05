"""
POO - Propriedades - Properties

Em linguagens de programação como Java, ao declararmos atributos privados nas classes, costumamos criar métodos
públicos para manipulação desses atributos. Esses métodos são conhecidos como getters e setters, onde os getters
retornam o valor do atributo, e os setters alteram o valor do mesmo.
"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property  # Esta propriedade pega o valor (get)
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_valor):
        self.__limite = novo_valor

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta("Felicity", 3000, 5000)
conta2 = Conta("Angelina", 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(soma)
