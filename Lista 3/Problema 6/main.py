num_alunos = int(input())

nome_maior_media = ""
maior_media = -1.0  

for i in range(num_alunos):
    nome = input()
    
    n1, n2 = map(float, input().split())

    media = n1 * 0.3 + n2 * 0.7

    if media > maior_media:
        maior_media = media
        nome_maior_media = nome

print(nome_maior_media)