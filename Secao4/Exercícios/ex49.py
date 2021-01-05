import datetime
tempo = input("Digite o tempo no formato 00:00:00: ")
adicionar = input("Digite quanto segundos foi a experiência: ")
x = datetime.datetime.strptime(tempo, '%H:%M:%S')
resultado = x + datetime.timedelta(seconds=int(adicionar))
print(resultado.time())
