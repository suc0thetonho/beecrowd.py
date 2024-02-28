A,B,C = input().split()
D,E,F = input().split()

QUANTI1=int(B)
VALOR1=float(C)

QUANTI2= int(E)
VALOR2= float(F)

result = (QUANTI1*VALOR1)+(QUANTI2*VALOR2)

print("VALOR A PAGAR: R$ {:.2f}".format(result))