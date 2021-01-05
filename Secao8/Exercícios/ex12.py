def somar(num):
    num = str(num)
    result = 0
    for i in num:
        result = result + int(i)
    return result


print(somar(123))
print(somar(251))
