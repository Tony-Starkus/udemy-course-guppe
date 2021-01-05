comprimento = float(input("Digite o comprimento do terreno: "))
largura = float(input("Digite a largura do terreno: "))
preco = float(input("Digite o preço do metro da tela: "))
print(f"O custo para cercar o terreno é: {((comprimento * 2) * preco) + ((largura * 2) * preco)}")
