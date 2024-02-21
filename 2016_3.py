shoes = input()
size = int(input())

if shoes == "M":
    if size < 44:
        size -= 34.5
    else:
        size -= 35
if shoes == "L":
    if size < 40:
        size -= 31.5
    else:
        size -= 32
print(size)
