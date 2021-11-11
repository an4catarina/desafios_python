salario = float(input())

if salario <= 2000.00:
    print('Isento')
    
elif salario <= 3000.00:
    valor = salario - 2000
    ir = valor * 0.08
    print(f'R$ {ir:.2f}')

elif salario <= 4500.00:
    valor = salario - 3000
    i8 = 1000 * 0.08
    ir = (valor * 0.18) + i8
    print(f'R$ {ir:.2f}')
    
else:
    valor = salario - 4500
    i8 = 1000 * 0.08
    i18 = 1500 * 0.18
    ir = (valor * 0.28) + i8 + i18
    print(f'R$ {ir:.2f}')