def intercalar(str1, str2):
    str1 = list(x for x in str1)
    str2 = list(x for x in str2)
    menor = str1 if len(str1) < len(str2) else str2
    for i in range(len(menor)):
        if menor == str1:
            str2.insert(i + i, str1[i])
    print(str2)


a = "tudo bem"

intercalar("oi", "tudo bem")
