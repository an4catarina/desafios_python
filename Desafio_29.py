NV = 0
med = 0

while NV < 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        NV += 1
        med += nota
    if nota < 0 or nota > 10:
        print('nota invalida')

media = med/2
print(f'media = {media}')