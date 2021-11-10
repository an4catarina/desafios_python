h1, m1, h2, m2 = input().split()
h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

TempoInicial = (h1*60)+m1
TempoFinal = (h2*60)+m2
Duracao = TempoFinal - TempoInicial

if Duracao < 0:
    Duracao += 24

if Duracao == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(f"O JOGO DUROU {Duracao//60} HORA(S) E {Duracao%60} MINUTO(S)")