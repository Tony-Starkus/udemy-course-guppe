"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos representar
             computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância.
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributos de instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utilizado para a construção do objeto.
"""


# Classes com atributos de instância público
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados
# Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público.
# Em Python, um atributo privado é definido com "__" duplo underscore no inicio do nome. Isso se chama Name Mangling.


class Acesso:

    def __init__(self, email, senha):
        self.email = email  # Atributo Público
        self.__senha = senha  # Atributo Privado

    def mostrar_senha(self):
        print(self.__senha)

    def mostrar_email(self):
        print(self.email)


user = Acesso('user@gmail.com', '123456')
print(user.email)
# print(user.__senha)  # AttributeError: 'Acesso' object has no attribute '__senha'
print(user._Acesso__senha)  # 123456

user.mostrar_email()
user.mostrar_senha()

# Atributos de Classe
p1 = Produto('Playstation 4', 'Video Game', 2300)  # Exemplo de atributo de instância.
p2 = Produto('Xbox S', 'Video Game', 4500)  # Exemplo de atributo de instância.


# Atributos de classe são atributos declarados fora do construtor, diretamente na classe. Geralmente, já inicializado
# com um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada instância
# ter seus próprios valores, como é o caso dos atributos de instância,  com os atributos de classe, todas as instâncias
# terão o mesmo valor para este atributo

# Refatorando a classe Produto

class Produto:
    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


p1 = Produto('Playstation 4', 'Video Game', 2300)  # Exemplo de atributo de instância.
p2 = Produto('Xbox S', 'Video Game', 4500)  # Exemplo de atributo de instância.
print(p1.id, p1.valor)
print(p2.id, p2.valor)
print(Produto.imposto)
print(p1.__dict__)

del p1.descricao

print(p1.__dict__)
