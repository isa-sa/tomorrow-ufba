Q1, Q2, Q3 = map(int, input().split())
E1, E2, E3 = map(int, input().split())

coletados = Q1 + Q2 + Q3
envenenados = E1 + E2 + E3
resgatados = (E1*2) + (E2*2) + (E3*2)

sobra = coletados - envenenados - resgatados
print(sobra)