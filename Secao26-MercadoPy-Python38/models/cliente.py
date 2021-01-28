from datetime import date, datetime


def date_para_str(data: date) -> str:
    return data.strftime("%d/%m/%Y")


def str_para_date(data: str) -> date:
    return datetime.strptime(data, "%d/%m/%Y")


class Cliente:
    contador: int = 101

    def __init__(self, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__data_nascimento = str_para_date(data_nascimento)
        self.__data_cadastro = date.today()
        Cliente.contador += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def email(self) -> str:
        return self.__email

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def data_nascimento(self) -> str:
        return date_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self) -> str:
        return date_para_str(self.__data_cadastro)

    def __str__(self) -> str:
        return f"Código: {self.codigo}\n" \
               f"Nome: {self.nome}\n" \
               f"Data de Nascimento: {self.data_nascimento}\n" \
               f"Cadastro: {self.data_cadastro}"
