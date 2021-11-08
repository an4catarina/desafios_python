N = int(input())


print(N)

cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedula in cedulas:
    print(f'{int(N / cedula)} nota(s) de R$ {cedula},00')
    N %= cedula