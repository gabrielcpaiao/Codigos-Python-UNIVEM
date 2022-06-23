#S POSSIVEL FORMAR
# N PARA N POSSIVEL
#selecionar 3 dentre as quatros
A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
if (((A< B + C) and (B<C+A) and (C<B+A)) or((A<B + D) and (B<A+D) and (D<A +B)) or((C< A + D) and (A<C+D) and (D<A +C)) or((B< D + C) and (C<B+D) and (D<C+B))):
    print("S")
else:
    print("N")