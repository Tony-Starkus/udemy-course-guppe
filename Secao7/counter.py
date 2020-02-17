"""
Módulo Collections - Counter (Counter)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
           com um dicionário, contendo como chave o elemento da lista e como valor a quantidade de ocorrências
           desse elemento.



# Utilizando o Counter
# Importar:
from collections import Counter
# Exemplo 1
# Podemos utilizar qualquer iterável. Aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]
res = Counter(lista)  # Utilizando o Counter()
print(type(res))
print(res)  # Ele vai contar quantos vezes cada número repete, agrupa isso, e mostra dentro de um dicionário.


# Exemplo 2
print(Counter('Geek University'))

"""

from collections import Counter
texto = """Nova Iorque ou Nova York (em inglês: New York) é a cidade mais populosa dos Estados Unidos e o centro da 
Região Metropolitana de Nova Iorque, uma das áreas metropolitanas mais populosas do mundo. 
É também a terceira cidade mais populosa da América, atrás de São Paulo e Cidade do México. 
A cidade exerce um impacto significativo sobre o comércio, finanças, mídia, arte, moda, pesquisa, tecnologia, educação 
e entretenimento de todo o planeta. Nova Iorque abriga a sede da Organização das Nações Unidas (ONU), sendo um 
importante centro para assuntos internacionais e amplamente considerada como a capital cultural do mundo. 
A cidade também é referida como Cidade de Nova Iorque (em inglês: New York City) para distingui-la do estado de
Nova Iorque, do qual faz parte.
Localizada em um dos maiores portos naturais do mundo, a cidade é composta por cinco boroughs: Bronx, Brooklyn, 
Manhattan, Queens e Staten Island. Com uma população que, de acordo com o Censo dos Estados Unidos de 2010,
atinge 8.175.133 habitantes, distribuídos numa área de terra de apenas 784 km². 
Nova Iorque é a grande cidade mais densamente povoada dos Estados Unidos e a segunda localidade mais densamente 
povoada do estado de Nova Iorque. Com cerca de 800 idiomas diferentes falados em seu território, Nova Iorque é a 
cidade com a maior diversidade linguística do mundo. A população da Região Metropolitana de Nova Iorque é a maior
dos Estados Unidos, estimada em cerca de 18,9 """
print(Counter(texto.split()))
print(Counter(texto.split()).most_common(5))  # Mostrando as 5 palavras com mais ocorrências no texto.
