from typing import List, Dict
from time import sleep


# /models/produto.py
class Produto:
    contador: int = 1

    def __init__(self, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> str:
        return self.__preco

    def __str__(self) -> str:
        return f"Código: {self.codigo}\nNome: {self.nome}\n"


# /models/produto.py


ps4: Produto = Produto("Playstation 4", 1789.44)
xbox: Produto = Produto("Xbox 360", 1699.00)

print(ps4)
print(xbox)

# main


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print("======================================")
    print("============ Bem-vindo(a) ============")
    print("============= Geek Shop ==============")
    print("============= Geek Shop ==============")
    print("Selecione uma opção abaixo:")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produto")
    print("4 - Visualizar carrinho")
    print("5 - Fechar pedido")
    print("6 - Sair do sistema")

    opcao = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Volte sempre!")
        sleep(2)
        exit(0)
    else:
        print("Opção inválida!")
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print("Cadastro de Produto")
    print("===================")

    nome: str = input("Informe o nome do produto: ")
    produto: Produto = Produto(nome, preco := float(input("Informe o preço do produto: ")))
    produtos.append(produto)
    print(f"O produto {produto.nome} foi cadastrado com sucesso!")
    sleep(2)
    menu()


def listar_produtos() -> None:
    if produtos:
        print("Listagem de produtos")
        print("--------------------")
        for produto in produtos:
            print(produto)
            print("-----------")
            sleep(2)
    else:
        print("Ainda não existem produtos cadastrados.")
    sleep(2)
    menu()


def comprar_produto() -> None:
    if produtos:
        print("Informe o código do produto que deseja adicionar ao carrinho.")
        print("-------------------------------------------------------------")
        print("==================== Produtos Disponíveis ===================")

        for produto in produtos:
            print(produto)
            print("------------------------------------")
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if carrinho:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f"O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.")
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    carrinho.append({produto: 1})
                    print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                    sleep(2)
                    menu()
            else:
                carrinho.append({produto: 1})
                print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                sleep(2)
                menu()
        else:
            print(f"O produto com código {codigo} não foi encontrado")
            sleep(2)
            menu()

    else:
        print("Ainda não existem produtos para vender.")
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if carrinho:
        print("Produtos no carrinho")

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                print("----------------------")
                sleep(1)

    else:
        print("Ainda não existem produtos no carrinho.")
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if carrinho:
        valor_total: float = 0
        print("Produtos do carrinho")

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                valor_total += dados[0] * dados[1]
                sleep(1)
        print(f"Sua fatura é R$ {valor_total}")

    else:
        print("Ainda não existem produtos no carrinho.")
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = Produto
            break
    return p


if __name__ == "main":
    main()
main()
