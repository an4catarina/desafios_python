rodadas = int(input())
T = 0
for rodada in range(rodadas):
    T += 1
    rodada = input()
    if ((rodada == 'papel pedra') or (rodada == 'pedra tesoura') or (rodada == 'pedra lagarto') or (rodada == 'spock pedra') or (rodada == 'tesoura papel') or (rodada == 'lagarto papel') or (rodada == 'papel spock') or (rodada == 'tesoura lagarto') or (rodada == 'spock tesoura') or (rodada == 'lagarto spock')):
        print(f'Caso #{T}: Bazinga!')
    if ((rodada == 'pedra papel') or (rodada == 'tesoura pedra') or (rodada == 'lagarto pedra') or (rodada == 'pedra spock') or (rodada == 'papel tesoura') or (rodada == 'papel lagarto') or (rodada == 'spock papel')  or (rodada == 'lagarto tesoura') or (rodada == 'tesoura spock') or (rodada == 'spock lagarto')):
        print(f'Caso #{T}: Raj trapaceou!')
    if (rodada == 'papel papel') or (rodada == 'pedra pedra') or (rodada == 'tesoura tesoura') or (rodada == 'lagarto lagarto') or (rodada == 'spock spock'):
        print(f'Caso #{T}: De novo!')
