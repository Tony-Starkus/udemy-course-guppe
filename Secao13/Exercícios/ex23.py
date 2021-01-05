
with open("ex_22_emp.txt", "w") as file:
    for i in range(5):
        dados = input("Informe a profissão e o tempo de serviço (em anos) separados por espaço: ").split(" ")
        file.write(f"{dados[0]},{dados[1]}\n")
    print("Done!")
