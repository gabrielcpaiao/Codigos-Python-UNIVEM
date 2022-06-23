#número ascendentes menores que 1000 (algarismos em ordem crescente (138) 1<3 e 3<8).
for i in range(1,1001):
    if(i//1000 < (i%1000)//100 and (i%1000)//100 < ((i%1000)%100)//10 and ((i%1000)%100)//10 < i%10):
        print(f"{i}", end=" ")