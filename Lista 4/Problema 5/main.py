nome = input()
vagas = int(input())
aprovados = []

for i in range(vagas):
    ap = input()
    aprovados.append(ap)

if nome in aprovados:
    print("PARABENS")
    
else:
    print("Vamos esperar a 2a chamada")