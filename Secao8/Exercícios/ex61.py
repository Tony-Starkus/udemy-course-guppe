def anagrama(str1, str2):
    if len(str1) != len(str2):
        return False

    d1 = {}
    d2 = {}

    for x in str1.lower():
        if x in d1:
            d1.update({x: d1[x] + 1})
        else:
            d1.update({x: 1})

    for x in str2.lower():
        if x in d2:
            d2.update({x: d1[x] + 1})
        else:
            d2.update({x: 1})

    for k in d1:
        if d1[k] != d2[k]:
            return False

    return True


print(anagrama("romA", "amor"))
print(anagrama("ANa", "ann"))
