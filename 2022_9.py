l = int(input())
w = int(input())

while w>0:
    res = w
    w = l % w
    l = res
print(l)

