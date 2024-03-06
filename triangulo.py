A,B,C = map(float,input().split())



if (A+B) > C and (A+C)>B and (C+B)>A:
    soma = A + B + C
    print("Perimetro = {:.1f}".format(soma))
else:
    area = (A+B)*C/2
    print("Area = {:.1f}".format(area))
    