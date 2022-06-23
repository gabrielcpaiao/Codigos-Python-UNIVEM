#Gabriel Costa Paião ra:618764
print("="*50)
print("Cálculo do produto vetorial")
print("="*50)

v0 = ["i","j","k"]

v1 = [0]*3
for a in range(3):
    v1[a] = int(input(f"Digite o valor da {a+1}º coordenada do vetor 1: "))
print()
v2 = [0]*3
for b in range(3):
    v2[b] = int(input(f"Digite o valor da {b+1}º coordenada do vetor 2: "))

i = (((v1[1])*(v2[2])))-(((v1[2])*(v2[1])))
j = (((v1[2])*(v2[0])))-(((v1[0])*(v2[2])))
k = (((v1[0])*(v2[1])))-(((v1[1])*(v2[0])))
print()
print(f"Resultado: {i}{v0[0]} + ({j}{v0[1]}) + ({k}{v0[2]})")