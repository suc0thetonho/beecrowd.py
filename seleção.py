A,B,C,D = input().split()

V_A = int(A)
V_B = int(B)
V_C = int(C)
V_D = int(D)

AB = V_A + V_B
CD = V_C + V_D

if V_B > V_C and V_D > V_A and CD > AB and V_C > 0 and V_D > 0 and V_A % 2 == 0:

    print("Valores aceitos")

else:

    print("Valores nao aceitos")