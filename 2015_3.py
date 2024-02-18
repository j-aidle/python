y = int(input())
name = input()

count=0

for i in range(1,y+1):
    if i <= 2:
        count+=10
    elif i > 2:
        count+=4
print(name," is ", count, " human years old", sep="")