VALOR = float(input())

if VALOR < 0 or VALOR > 100:
    print("Fora de intervalo")

elif VALOR >= 0 and VALOR <= 25:
    print("Intervalo [0,25]")

elif VALOR > 25 and VALOR <= 50:
    print("Intervalo [25,50]")

elif VALOR > 50 and VALOR <= 100:
    print("Intervalo [75,100]")