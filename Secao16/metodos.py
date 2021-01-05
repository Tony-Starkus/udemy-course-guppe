"""
packages {
    $ pip3 install passlib
}
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar.

Em Python, dividimos os métodos em 2 grupos: Métodos de instância e Métodos de Classe

# Nomes compostos para métodos são separados por underline

OBS: Quando um método não utiliza nenhum atributo da instância, é recomendado que ele seja um método de classe, com o
uso do decordor @classmethod
"""
from passlib.hash import pbkdf2_sha256 as cryp


# MÉTODOS DE INSTÂNCIA
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        """
        O método __init__(self) é um método especial chamado de Construtor, e sua função é construir o objeto a partir
        da classe.
        """
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


p1 = Produto('Playstation4', 'Video Game', 2300)
print(p1.desconto(20))
print(Produto.desconto(p1, 20))  # Outra forma de fazer. Produto.desconto(self, desconto)


# MÉTODOS DE CLASSE
class Usuario:

    contador = 0

    @classmethod  # Este decorador define que o método abaixo é um método de classe.
    def conta_usuarios(cls):
        print(f"Temos {cls.contador} usuários no sistema")

    # MÉTODOS ESTÁTICOS
    @staticmethod  # Este decorador define o método abaixo como um método estático
    def definicao():
        return "UXR344"

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha)
        Usuario.contador = self.__id
        print(f"Usuário criado: {self.__gera_usuario()}")

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        """Verifica se a senha passada no parâmetro está correto."""
        if cryp.verify(senha, self.__senha):
            return True
        return False

    # Método Privado
    def __gera_usuario(self):
        """Somente a classe pode acessar. Nem a instância acessa ele"""
        return self.__email.split("@")[0]


user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())
print(Usuario.nome_completo(user1))

print(f"Senha User1: {user1._Usuario__senha}")
print(f"Senha User2: {user2._Usuario__senha}")
print(user1.checa_senha("123456"))

Usuario.conta_usuarios()  # Forma correta

