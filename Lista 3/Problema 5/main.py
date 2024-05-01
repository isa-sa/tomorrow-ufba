k, j = map(int, input().split())

a, b = 0, 1
soma = 0

for i in range(j + 1):
    if k <= i:
        soma += a
    a, b = b, a + b

print(soma)