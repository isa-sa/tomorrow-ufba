N = int(input())
while not (1 <= N <= 100):
    N = int(input())

numeros_F = []

for i in range(N):
    F = int(input())
    
    while not (0 <= F <= 9):
        F = int(input())
    
    numeros_F.append(F)

if 1 in numeros_F and 2 in numeros_F:
    print("Equipe Balanceada")
else:
    print("Equipe Desbalanceada")