initial = input()
iter = input()
suma = int(initial)

for x in range(int(iter)):
    l = len(str(suma))
    aux = 0
    for i in range(l):
        numero = str(suma)
        aux += int(numero[i])
        if i == l-1:
            suma += aux
print(suma)