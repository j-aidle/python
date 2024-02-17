x = input()
vec = []
totalProduct = 1
totalSum = 0
res1 = ""
res2 = ""

while x !="#":
    vec.append(int(x))
    x = input()

for i in vec:
    totalProduct *=int(i)
    totalSum += int(i)

for i in vec:
    res1 += str(totalSum-int(i)) + " "
    res2 += str(totalProduct//int(i)) + " "    
    
print(res1)
print(res2)