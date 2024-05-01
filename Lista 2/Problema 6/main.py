C, c, X = map(int, input().split())
C, c, X = int(C), int(c), int(X)
volumeGrande = C^3
volumeMenor = (c^3)*X

if volumeMenor >= volumeGrande:
    print("Eh possivel")

else:
    print("!Eh possivel")