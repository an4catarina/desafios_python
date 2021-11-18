X, Y = list(map(int, input().split()))

while X != Y:
    if X > Y:
        print('Decrescente')
    else:
        print('Crescente')
    X, Y = list(map(int, input().split()))