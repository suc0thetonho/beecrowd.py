abc = input("").split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("{:.3f} m2".format(area))