"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para e trabalhar com data e hora chamado 'datetime'
"""
import datetime

print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e hora corrente
print(datetime.datetime.now())  # 2020-10-20 13:54:07.841293
print(repr(datetime.datetime.now()))

# replace() -> para fazer ajustes na data/hora

inicio = datetime.datetime.now()
print(f"Início: {inicio}")

# Alterar o horário para 16 horas, 0 minutos, 0 segundos e 0 microssegundos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

# Criando datetime
evento = datetime.datetime(2020, 1, 1, 0)  # year, month, day, hour
print(evento)

data_nascimento = "22/07/1999".split("/")
print(f"data_nascimento: "
      f"{datetime.datetime(int(data_nascimento[2]), int(data_nascimento[1]), int(data_nascimento[0]))}")

print(evento.year)
