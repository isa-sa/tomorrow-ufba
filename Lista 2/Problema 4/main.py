N, Q = input().split()
N, Q = int(N), int(Q)

if Q > N and (Q - N) % 2 == 0:
    print("vendido")   
else:
    print("sinto muito")