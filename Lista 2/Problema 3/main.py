N = int(input())

vermelho = 0
azul = 0
amarelo = 0

for i in range(N):
    if i % 3 == 0:
        vermelho += 1
    elif i % 3 == 1:
        azul += 1
    else:
        amarelo += 1

print("Vermelho", vermelho)
print("Azul", azul)
print("Amarelo", amarelo)