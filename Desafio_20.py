salario = float(input())

if salario <= 400.00:
    reajuste = 15

elif salario <= 800.00:
    reajuste = 12

elif salario <= 1200.00:
    reajuste = 10

elif salario <= 2000.00:
    reajuste = 7

else:
    reajuste = 4

reajustetot = salario * reajuste/100
novosalario = salario + reajustetot


print(f"Novo salario: {novosalario:.2f}")
print(f"Reajuste ganho: {reajustetot:.2f}")
print(f"Em percentual: {reajuste} %")
    