N, XP = input().split()
N = int(N)
XP = int(XP)
XPYoda, XPLuke, XPAh = map(int, input().split())

novoXp = N*XP
print('Yoda', XPYoda + novoXp)
print('Luke', XPLuke + novoXp)
print('Ahsoka', XPAh + novoXp)