A,B=(input().split())
C,D=(input().split())

X1=float(A)
Y1=float(B)
X2=float(C)
Y2=float(D)

result_x= X2-X1
result_y= Y2-Y1

result_1= (result_x*result_x)+(result_y*result_y)

result = result_1 ** (1/2)

print("{:.4F}".format(result))



