tipo = input()
classe = input()
alimentar = input()

if (tipo == 'vertebrado'):
    if (classe == 'ave'):
        if (alimentar == 'carnivoro'):
            print('aguia')
        if (alimentar == 'onivoro'):
            print('pomba')

    if (classe == 'mamifero'):
        if (alimentar == 'onivoro'):
            print('homem')
        if (alimentar == 'herbivoro'):
            print('vaca')

if (tipo == 'invertebrado'):
    if (classe == 'inseto'):
        if (alimentar == 'hematofago'):
            print('pulga')
        if (alimentar == 'herbivoro'):
            print ('lagarta')

    if (classe == 'anelideo'):
        if (alimentar == 'hematofago'):
            print('sanguessuga')
        if (alimentar == 'onivoro'):
            print('minhoca')