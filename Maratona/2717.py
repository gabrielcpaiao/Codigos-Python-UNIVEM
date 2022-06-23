#min para fabricar um presente
#faltam N min p ir embora e 2 presente p fazer  fabricar hoje ou deixar p manhã
#"Farei hoje!"
#"Deixa para amanha!"
# if (2 <= N <= 100 and (1 <= A, B <= 100)):
N = int(input())
SA, SB = input().split()
A = int(SA)
B = int(SB)
if (A + B <= N):
    print("Farei hoje!")
else:
    print("Deixa para amanha!")