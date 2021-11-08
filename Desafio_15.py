Pedido = input()
Numero, Quantidade = Pedido.split()

Numero = int(Numero)
Quantidade = int(Quantidade)

if Numero == 1:
    Total = 4.00  * Quantidade
    print(f"Total: R$ {Total:.2f}")
elif Numero == 2:
    Total = 4.50 * Quantidade
    print(f"Total: R$ {Total:.2f}")
elif Numero == 3:
    Total = 5.00 * Quantidade
    print(f"Total: R$ {Total:.2f}")
elif Numero == 4:
    Total = 2.00 * Quantidade
    print(f"Total: R$ {Total:.2f}")
elif Numero == 5:
    Total = 1.50 * Quantidade
    print(f"Total: R$ {Total:.2f}")
