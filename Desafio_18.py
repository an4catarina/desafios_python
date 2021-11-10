horarios = input()
H1 = int(horarios.split()[0])
H2 = int(horarios.split()[1])

if H1 < H2:
    final = H2 - H1
else:
    final = (H2-H1)+24

print(f"O JOGO DUROU {final} HORA(S)")

