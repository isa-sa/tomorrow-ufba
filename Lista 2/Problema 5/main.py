X, Y = input().split()
X, Y = int(X), int(Y)
    
if 0 < X < 71 and 0 < Y < 71:
    print("Coordenada valida e o navio esta perto")

elif 70 < X < 100 or 100 > Y > 70:
    print("Coordenada valida e o navio esta longe")
    
if 0 >= X or X >= 100 or 0 >= Y or Y >= 100:
    print("Coordenada invalida")