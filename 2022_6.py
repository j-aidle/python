count = 0

a = int(input())

for i in range(a):
    if str(i).find("5") != -1:
        count+=str(i).count("5")
print(count)