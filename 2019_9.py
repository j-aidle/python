a = input()

# reemplacem les r en espai per doble r
a = a.replace('r ', 'rr ')
a = a.replace('R ', 'RR ')

#si hi ha una r al final afegim una r al final
if a[-1] == 'r' or a[-1] == 'R':
    a += a[-1] 

print(a)