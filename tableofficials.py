import string


x = int(input())
y = int(input())
z = int(input())
t = int(input())

res = x+(2*y)+(3*z)
pct = 100*((x+y+z))/t

print(res,'',round(pct),'%')