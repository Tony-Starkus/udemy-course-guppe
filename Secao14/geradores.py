"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo Iterador é um Generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradores utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)
-----------------------------------------------------------------------------------------------
| Funções                                             | Generator Functions
-----------------------------------------------------------------------------------------------
| Utilizam return                                     | Utilizam yield
-----------------------------------------------------------------------------------------------
| Retorna uma vez                                     | Podem utilizar yield multiplas vezes
-----------------------------------------------------------------------------------------------
| Quando executada, retorna um valor                  | Quando executada, retorna um generator
-----------------------------------------------------------------------------------------------
"""


# Exemplo de Generator Function (Função Geradora)


def conta_ate(valor_maximo):
    """
    O yield retorna o valor, e espera o next() para continuar. No caso, no next(), ele incrementa o contador, retorna
    ele e espera o próximo next(), sempre querificando se o while é True.
    :param valor_maximo:
    :return:
    """
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


# OBS: Um Generator Function não é um Generator, ela gera um generator
gen = conta_ate(5)
print(type(gen))  # Retorna: <class 'generator'>
print(next(gen))  # Retorna: 1
print(next(gen))  # Retorna: 2
print(next(gen))  # Retorna: 3
print(next(gen))  # Retorna: 4
print(next(gen))  # Retorna: 5

gen = conta_ate(10)

for num in gen:
    print(num)
