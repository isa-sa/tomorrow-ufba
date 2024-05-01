X, Y = input().split()
X, Y = int(X), int(Y)
difusorPorMetro = int(Y)*9
areaFalta = X - difusorPorMetro
difusorFalta = (areaFalta + 8) // 9

if difusorPorMetro >= X:
    print("Lar doce lar.")
    
else:
    print("Precisa de mais difusores!")
    print(difusorFalta)