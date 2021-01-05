"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

dunder init -> __init__()

Dunder -> Double Underscore

__repr__() -> Representação do objeto para o desenvolvedor
    def __repr__(self):
        return f"{self.titulo} escrito por {self.autor}"
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f"{self.titulo} escrito por {self.autor}"

    def __len__(self):
        return self.paginas

    def __del__(self):
        print("Um objeto do tipo Livro foi deletado da memória")

    # Somatório
    def __add__(self, other):
        return f"{self} - {other}"

    # Multiplicação
    def __mul__(self, other):
        if isinstance(other, int):
            msg = ""
            for n in range(other):
                msg += "|" + str(self)
            return msg
        return "Não posso multiplicar"


livro1 = Livro("Python Rocks!", "Geek Unviersity", 400)
livro2 = Livro("Inteligência Artificial com Python", "Geek University", 350)

print(livro1)
print(str(len(livro1)) + " páginas")

print(livro2)
print(str(len(livro2)) + " páginas")

print(livro1 + livro2)

print(livro1 * 3)
