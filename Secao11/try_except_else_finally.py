"""
Try / Except / Else / Finally

Dica de quanto e onde tratar código:
TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.


# else -> É executado somente se não ocorrer o erro.
try:
    num = int(input("Informe um número: "))
except ValueError:
    print('Valor incorreto')
else:
    print(f"Você digitou: {num}")



# Finally
try:
    num = int(input("Informe um núero: "))
except ValueError:
    print("Você não digitou um valor válido")
else:
    print(f"Você digitou o número {num}")
finally:
    print("Executando o finally")

# O bloco 'finally' é SEMPRE executado independente se aconteceu exceção ou não.
# O finally geralmene é utilizado para fechar ou desalocar recursos.
"""

# Exemplo mais complexo


def dividir(a, b):
    """try:
        return int(a) / int(b)
    except ValueError:
        return "Valor incorreto"
    except ZeroDivisionError:
        return "Não é possível realizar uma divisão por 0"""
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as error:
        return f"Ocorreu um problema: {error}"


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

print(dividir(num1, num2))
