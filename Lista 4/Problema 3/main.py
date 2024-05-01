N, Q = map(int, input().split())

categorias = {i: 0 for i in range(N)}

numeros = map(int, input().split())
for R in numeros:
    categoria = R % N
    categorias[categoria] += 1

print(f"Mod {N}")
for i in range(N):
    print(f"{i}: {categorias[i]}")