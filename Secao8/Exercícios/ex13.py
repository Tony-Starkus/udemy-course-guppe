def calcular(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    else:
        return "Operação inválida!"


print(calcular(1, 2, "+"))
print(calcular(4, 2, "/"))
print(calcular(3, 5, "*"))
print(calcular(1, 2, "-"))
