nota_s = input()

nota =  int(nota_s)

nota100 = nota//100
nota -= nota100*100

nota50 = nota//50
nota -= nota50*50

nota20 = nota//20
nota -= nota20*20

nota10 = nota//10
nota -= nota10*10

nota5= nota//5
nota -= nota5*5

nota2= nota//2
nota -= nota2*2

nota1 = nota//1
nota -= nota1*1

print(nota_s)
print (nota100,"nota(s) de R$ 100,00")
print (nota50,"nota(s) de R$ 50,00")
print (nota20,"nota(s) de R$ 20,00")
print (nota10,"nota(s) de R$ 10,00")
print (nota5,"nota(s) de R$ 5,00")
print (nota2,"nota(s) de R$ 2,00")
print (nota1,"nota(s) de R$ 1,00")
