N = int(input())
nomes = []

for i in range(N):
    S = input()
    nomes.append(S)
    
playlist = sorted(nomes)

for nome in playlist:
    print(nome)