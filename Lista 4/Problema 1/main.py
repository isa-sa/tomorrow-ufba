N = int(input())

filaFok = []
filaMok = []

for i in range(N):
    entrada = input().split()
    nome = entrada[0]
    genero1 = entrada[1]

    entrada2 = input().split()
    nome2 = entrada2[0]
    genero2 = entrada2[1]

    if genero1 == 'M':
        filaFok.append(nome)
    elif genero1 == 'H':
        filaMok.append(nome)

    if genero2 == 'M':
        filaFok.append(nome2)
    elif genero2 == 'H':
        filaMok.append(nome2)

    if not filaFok:
        filaFok.append('Vazia')

    if not filaMok:
        filaMok.append('Vazia')

print('Fila Feminina:', *filaFok, sep='\n')
print('Fila Masculina:', *filaMok, sep='\n')