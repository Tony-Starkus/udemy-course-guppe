def desenha_linha(x):
    result = ""
    for i in range(x):
        result = result + "="
    return result


print(desenha_linha(2))
print(desenha_linha(10))
