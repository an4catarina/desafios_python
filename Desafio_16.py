N1, N2, N3, N4 = input().split()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = (N1*2 + N2*3 + N3*4 + N4)/10
print("Media", f"{(media):.1f}")

if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print('Aluno reprovado.')
    
else:
    print('Aluno em exame.')
    NE = float(input())
    print("Nota do exame:", f"{(NE):.1f}")
    Media2 = (media+NE)/2
    
    if Media2 >= 5.0:
        print("Aluno aprovado.")
        print("Média final:", f"{(Media2):.1f}")
    else:
        print("Aluno reprovado.")
        print("Média final:", f"{(Media2):.1f}")