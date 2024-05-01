tipoAtq = input()
tipoDef = input()

relacoes_tipos = {
    "água": ["besta", "fogo"],
    "besta": ["planta", "solo"],
    "fogo": ["besta", "planta"],
    "planta": ["água", "solo"],
    "raio": ["água", "besta", "planta"],
    "solo": ["água", "fogo", "raio"]
}

if tipoDef in relacoes_tipos[tipoAtq]:
    print("hit!")

else:
    print("countered!")