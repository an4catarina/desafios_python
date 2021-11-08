valor = float(input())

if float(0 <= valor <= 25):
    print('Intervalo [0,25]')
elif float(25 < valor <= 50):
    print('Intervalo (25,50]')
elif float(50 < valor <= 75):
    print('Intervalo (50,75]')
elif float(75 < valor <= 100):
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')


