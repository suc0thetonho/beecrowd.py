A,B,C,D =  map(float,input().split())

M = ((A*2)+(B*3)+(C*4)+D)/10

if M < 5.0:
    print("Media: {:.1f}".format(M))
    print("Aluno reprovado.")

elif M >= 7.0:
    print("Media: {:.1f}".format(M))
    print("Aluno reprovado.")

elif M >= 5.0 and M <= 6.9:
    N_F = float(input())
    M_F = (M+N_F)/2
    if M_F >= 5.0:
        print("Media: {:.1f}".format(M))
        print("Aluno em exame.")
        print("Nota do exame: {:.1f}".format(M_F))
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(M_F))
    elif M_F <= 4.9:
        print("Media: {:.1f}".format(M))
        print("Aluno em exame.")
        print("Nota do exame: {:.1f}".format(M_F))
        print("Aluno Reprovado.")
        print("Media final: {:.1f}".format(M_F))
