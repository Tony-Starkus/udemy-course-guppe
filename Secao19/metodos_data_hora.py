"""
Métodos de Data e Hora


agora = datetime.datetime.now()  # now == agora
print(f"agora: {agora}")
print(f"type(agora): {type(agora)}")
print(f"repr(agora): {repr(agora)}")

hoje = datetime.datetime.today()  # today == hoje
print(f"hoje: {hoje}")
print(f"type(hoje): {type(hoje)}")
print(f"repr(hoje): {repr(hoje)}")

# A diferença entre o now() e o today() é que o now() pode ser definido um timezone, e no today() não pode.




# Mudanças ocorrendo à meia-noite
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(f"manuntencao: {manutencao}")
print(f"type(manutencao): {type(manutencao)}")
print(f"repr(manutencao): {repr(manutencao)}")




# Encontrar o dia da semana: weekday()
# Os dias da semana do método weekday() começam em 0
# 0 -> segunda-feira
# 1 -> terça-feira
# 2 -> quarta-feira
# 3 -> quinta-feira
# 4 -> sexta-feira
# 5 -> sábado
# 6 -> domingo
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(f"manutencao.weekday(): {manutencao.weekday()}")




# Aniversário
aniversario = input("Qual a sua data de nascimento? dd/mm/yyyy: ")
aniversario = aniversario.split("/")
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
print(f"aniversario: {aniversario}")

if aniversario.weekday() == 0:
    print(f"Você nasceu na segunda-feira")
elif aniversario.weekday() == 1:
    print(f"Você nasceu na terça-feira")
elif aniversario.weekday() == 2:
    print(f"Você nasceu na quarta-feira")
elif aniversario.weekday() == 3:
    print(f"Você nasceu na quinta-feira")
elif aniversario.weekday() == 4:
    print(f"Você nasceu na sexta-feira")
elif aniversario.weekday() == 5:
    print(f"Você nasceu no sábado")
elif aniversario.weekday() == 6:
    print(f"Você nasceu no domingo")




# Formatando a data
hoje = datetime.datetime.now()
print(hoje)
hoje_formatado = hoje.strftime("%d/%m/%Y")
print(hoje_formatado)




# Transformando string em datetime
nascimento = input("Qual sua data de nascimento? dd/mm/yyyy: ")
nascimento = datetime.datetime.strptime(nascimento, "%d/%m/%Y")
print(nascimento)



almoco = datetime.time(12, 30, 0)  # hour, minute, seconds
print(almoco)
"""
import datetime, timeit, functools

# Marcando tempo de execução do código com timeit
# loop
tempo = timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000)  # number indica quantas vezes vai testar.
print(tempo)


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))  # partial(function, params), times_to_repeat
