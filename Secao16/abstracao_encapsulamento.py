"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -> cápsula

            Classe
----------------------------------
|                                |
|       Atributos e Métodos      |
|--------------------------------|

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado chamado
__falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas Python não bloqueia este acesso fora
da classe. Com Python acontece um fenômeno chamado Name Mangling, que faz uma alteração na forma de se acessar os
elementos privados, conforme:
_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:
instancia._Pessoa__nome
instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados
de usuário.
"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor precisa positivo")

    def sacar(self, valor):
        if self.__saldo >= valor > 0:
            self.__saldo -= valor
        else:
            print("Salvo insuficiente")

    def transferir(self, valor, conta_destino):
        # 1. Remover o valor da conta de origem
        if self.__saldo >= valor > 0:
            self.__saldo -= valor
        else:
            print("Salvo insuficiente")
            return
        # 2. Adicionar o valor na conta de destino
        conta_destino.__saldo += valor


# Testando
conta1 = Conta('Angelina', 150.00, 1500)
conta2 = Conta('Felicity', 300, 2000)
print(conta1.__dict__)
conta1.depositar(150)
print(conta1.__dict__)
conta1.sacar(200)
print(conta1.__dict__)

conta1.extrato()
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()
