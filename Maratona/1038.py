cod, qnt = input(). split()
c = float(cod)
q = float(qnt)
if (c == 1):
    total = 4* q
    print(f"Total: R$ {total:.2f}")
if(c == 2):
    total = 4.5* q
    print(f"Total: R$ {total:.2f}")
if(c == 3):
    total = 5* q
    print(f"Total: R$ {total:.2f}")
if(c == 4):
    total = 2* q
    print(f"Total: R$ {total:.2f}")
if(c == 5):
    total = 1.5* q
    print(f"Total: R$ {total:.2f}")