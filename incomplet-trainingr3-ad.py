cr = input()
nwb = int(input())
i=0
vect = []

while i !=nwb:
    x = input()
    vect.append(input())
    i+=1

res = []

for j in nwb:   
    size = vect[j].length()
    
    for k in size:        
        cont = False
        if (cr[k] == vect[j][k]):
            cont = True    
    if(cont==False):
        break;
if (cont):
    print('YES')
else:
    print('NO')