"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.
OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos e métodos
da classe herdada.

Cliente
    - Nome
    - Sobrenome
    - cpf
    - renda

Funcionario
    - Nome
    - Sobrenome
    - cpf
    - matricula

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a outras entidades?

OBS: Quando uma classe herda outra classe, ela herda TODOS os atributos e métodos da classe herdada

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;
Quando uma classe herda de outra classe, ela é conhecida por:
    [Cliente, Funcionário]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

# Sobrescrita de Métodos (Overriding)
Sobrescrita de Métodos, ocorre quando reecrevemos/reimplementamos um método presente na Super Classe em classes filhas.
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # NÃO É COMUM ACESSAR DADOS ASSIM
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # COMUM PARA ACESSAR DADOS
        self.__matricula = matricula

    # Sobrescrita de Métodos (Overriding)
    def nome_completo(self):
        print(super().nome_completo())
        return f"Funcionário: {self.__matricula} | Nome: {self._Pessoa__nome}"


cliente1 = Cliente("Angelina", "Jolie", "123-456-789-00", 5000)
funcionario1 = Funcionario("Felicity", "Jones", "987-654-321-11", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
