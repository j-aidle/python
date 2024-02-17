x = int(input())
i = 0
    
while x!=1:
    print(x, '->')

    if (x%2 == 0):
        x = x/2;

    else:
        x = (x*3)+1

    i+=1


print(x, '[',i,']') 

   