num = int(input())

ano = 365
anos = int(num/ano)
print(f'{anos} ano(s)')
resto = num%365

meses = 30
mes = int(resto/meses)
print(f'{mes} mes(es)')

dias = resto%30
print(f'{dias} dia(s)')