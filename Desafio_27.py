v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())
qtd = 0
soma = 0

valores = [v1, v2, v3, v4, v5, v6]

for v in valores:
    if v > 0:
        qtd += 1
        soma += v
media = soma/qtd
print(f'{qtd} valores positivos')
print(f'{media:.1f}')