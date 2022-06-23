while True:
    M, N = input().split()
    m = int(M)
    n = int(N)
    if m<=0 or n<=0:
        break
    if n<m:
        m,n = n,m
    x = 0
    vet = []
    for i in range(m, n+1):
        x += i
        vet.append(i)
    print(*vet,f"Sum={x}")