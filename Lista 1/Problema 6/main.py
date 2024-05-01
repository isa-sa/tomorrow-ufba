T, D = input().split()
V, P = input().split()
T, D = int(T), int(D)
V, P = int(V), int(P)

vezespedagio = int(T/D)
km = V*T
valorpedagio = vezespedagio*P
total = km + valorpedagio
print(total)