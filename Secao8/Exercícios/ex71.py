class Ponto:
    """This is a dot class in Cartesian Plan"""
    x = 0
    y = 0


def dentro_ret(_v1, _v2, _p):
    if v1.x <= _p.x <= _v2.x and _v1.y >= _p.y >= _v2.y:
        return 1
    else:
        return 0


v1 = Ponto()
v1.x = 1
v1.y = 5
v2 = Ponto()
v2.x = 5
v2.y = 1
p = Ponto()
p.x = 0
p.y = 4
print(dentro_ret(v1, v2, p))
