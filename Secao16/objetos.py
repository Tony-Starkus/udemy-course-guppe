"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de
uma classe como variáveis do tipo definido na classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def get_ligada(self):
        return self.__ligada

    def set_ligada(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def get_cliente(self):
        print(f"O cliente é {self.__cliente.get_nome()}")


class Usuario:

    def __init__(self, nome, sobrenome, cpf, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__email = email
        self.__senha = senha

    def get_nome(self):
        return self.__nome


lamp1 = Lampada('branca', 110, 60)
print(lamp1.get_ligada())
lamp1.set_ligada()
print(lamp1.get_ligada())

user1 = Usuario('Felicity', 'Jones', '819.819.819-89', 'felicity@gmail.com', '123456')
cc1 = ContaCorrente(5000, 20000, user1)
cc1.get_cliente()

