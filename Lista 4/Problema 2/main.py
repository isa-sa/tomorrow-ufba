sequencia1 = input()
sequencia2 = input()

if sequencia1 in sequencia2:
    posicao = sequencia2.index(sequencia1)
if sequencia1 in sequencia2:
    print(f"Plagio encontrado na posicao {posicao}!")
else:
    print("Nenhum plagio detectado!")
