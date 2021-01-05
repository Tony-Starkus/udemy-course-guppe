"""
JSON e Pickle

$  pip3 install jsonpickle

JSON -> JavaScript Object Notation

API - São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook, Youtube...) e terceiros
(Nós, desenvolvedores).


ret = json.dumps(['produto', {'Playstation4': ('2TB', 'Novo', '220V', 2340)}])
print(type(ret))
print(ret)



class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("Felix", "Vira-Lata")
ret = json.dumps(felix.__dict__)
print(ret)

ret = jsonpickle.encode(felix)
print(ret)

"""
import json
import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("Felix", "Vira-Lata")
with open("felix.json", "w") as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
