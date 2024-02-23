a = input().lower()

letters = "abcdefghijklmnopqrstuvwxyz"

for i in reversed(letters):
    count = 0
    for j in a:
        if i == j:
            count +=1
    print(i, "=", count)
