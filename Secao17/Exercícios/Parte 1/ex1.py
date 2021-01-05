
class Pessoa:

    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def imprimir(self):
        print(f"Nome: {self.nome} | Endereço: {self.endereco} | Telefone: {self.telefone}")


p1 = Pessoa("Thalisson Badeira Araújo", "Rio Branco, Acre, Brasil", "9285-8456")
p2 = Pessoa("Vanessa Silva", "Ufac, Rio Branco, Acre, Brasil", "9964-8489")
p1.imprimir()
p2.imprimir()
