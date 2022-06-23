d = {}
for letra in "abracadabra":
    if letra in d:
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1
print(d)

d = {}
for letra in "abracadabra":
    d[letra] = d.get(letra,0) + 1
    print(d)
