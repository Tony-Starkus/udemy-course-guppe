from sys import maxsize


def mdc(a, b):
    while b:
        a, b = b, a % b
    print(a)


mdc(20, 24)
