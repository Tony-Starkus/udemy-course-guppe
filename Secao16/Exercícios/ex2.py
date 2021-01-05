
class Agenda:

    limite = 10
    dados = dict()

    @classmethod
    def add_person(cls, nome, idade, altura):
        if nome not in cls.dados:
            cls.dados.update({nome: {idade, altura}})
        else:
            print("A pessoa já existe!")

    @classmethod
    def rmv_person(cls, nome):
        if nome in cls.dados.keys():
            cls.dados.pop(nome)
            print(f"{nome} foi excluído!")
        else:
            print("A pessoa não existe!")

    @classmethod
    def search_person(cls, nome):
        if nome in cls.dados:
            print(f"Posição: {list(cls.dados.keys()).index(nome)}")

    @classmethod
    def show(cls):
        for person, value in cls.dados.items():
            print(f"Nome: {person} | Idade: {list(value)[0]} | Altura: {list(value)[1]}")

    @classmethod
    def show_person(cls, i):
        nome = list(cls.dados)[i]
        print(f"Nome: {nome} | Idade: {list(cls.dados[nome])[0]} | Altura: {list(cls.dados[nome])[1]}")


agenda = Agenda()
agenda.add_person("Thalisson", 21, 1.65)
agenda.add_person("Vanessa", 22, 1.60)
agenda.add_person("Kamila", 18, 1.62)

agenda.show()

agenda.search_person("Thalisson")
agenda.rmv_person("Thalisson")
print(agenda.dados)

agenda.show_person(4)
