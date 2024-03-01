A,B,C = input().split()

VALOR_A = float(A)
VALOR_B = float(B)
VALOR_C = float(C)

# TRIANGULO
TRI = (VALOR_A*VALOR_C)/2

# CIRCULO
CIR = (VALOR_C*VALOR_C)*3.14159

# TRAPEZIO
TRA = ((VALOR_A+VALOR_B)*VALOR_C)/2

# QUADRADO
QUA = VALOR_B*VALOR_B

# RETANGULO
RET = VALOR_A*VALOR_B

print("TRIANGULO: {:.3F}".format(TRI))
print("CIRCULO: {:.3F}".format(CIR))
print("TRAPEZIO: {:.3F}".format(TRA))
print("QUADRADO: {:.3F}".format(QUA))
print("RETANGULO: {:.3F}".format(RET))
