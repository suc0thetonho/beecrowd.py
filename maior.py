A, B, C = input().split()

VALOR_A = int(A)
VALOR_B = int(B)
VALOR_C = int(C)

MAIORAB = (VALOR_A+VALOR_B+abs( VALOR_A-VALOR_B))/2
MAIORABC_ = (MAIORAB+VALOR_C+abs(MAIORAB-VALOR_C))/2
MAIORABC = int(MAIORABC_)

print(MAIORABC,"eh o maior")