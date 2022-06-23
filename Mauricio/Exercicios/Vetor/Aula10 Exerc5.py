v = []
for i in range(10):
    v.insert(i, int(input()))
print(v)
x = int(input(""))
if (x in v):
    print(f"{x} existe e aparece ")