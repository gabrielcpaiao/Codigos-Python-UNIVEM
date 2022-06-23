with open("dom_casmurro_cap_1.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha!\n")
    arquivo.write("Segunda linha.\n")
with open("dom_casmurro_cap_1.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Esta é a terceira linha!\n")
with open("dom_casmurro_cap_1.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read(), end=" ")