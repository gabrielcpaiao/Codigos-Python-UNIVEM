h, p, f, d = input().split()
he = int(h)
po = int(p)
fu = int(f)
di = int(d)

if ((he > fu > po) and (di == 1) or ((he > po > fu) and (di == -1)) or ((fu > po > he) and (di == 1)) or ((fu > he > po) and (di == -1)) or ((po > he > fu) and (di == 1)) or ((po > fu > he) and (di == -1))):
    print("S")
else:
    print("N")