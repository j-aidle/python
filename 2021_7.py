a = [input().lower()]

while len(a) > 1:
    l = a.pop(0)
    if l in a:
        print("Not an isogram")
        break

print("Isogram detected")


