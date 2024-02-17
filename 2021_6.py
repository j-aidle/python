count = 0

while True:
    
    a = input()
    
    if a == "#":
        break

    for i in range(len(a)):
        if a[i] == "o":
            count += 1
        elif a[i] == "+":
            count += 1.5
        elif a[i] == "T":
            count += 2

print(count)