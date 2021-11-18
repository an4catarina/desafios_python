N = int(input())

for x in range(N):
    texto = input().split()
    mensagem = ''

    for item in texto:
        mensagem = mensagem + item[0]
    print(mensagem)
    
    