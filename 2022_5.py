a = int(input())
x = []
y = []
m = 0 
n = 0

for i in range(a):
    c1,c2 = input().split()
    x.append(c1)
    y.append(c2)

for i in range(a):
    movey = int(y[i]) - m
    if movey>0:
        print("Walk", abs(movey), "steps north")
    elif movey < 0:
        print("Walk", abs(movey), "steps south")       
    movex = int(x[i]) - n
    if movex>0:
        print("Walk", abs(movex), "steps east")
    elif movex < 0:
        print("Walk", abs(movex), "steps west")
    m = int(y[i])
    n = int(x[i])