idade = int(input("Digite a idade: "))
ts = int(input("Digite o tempo de serviço (em anos): "))

if idade >= 64 or ts == 30 or (idade >= 60 and ts >= 25):
    print("Pode aposentar")
else:
    print("Não pode aposentar")
