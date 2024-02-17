numbers = []
missing = []

for i in range(3):
    line = input().split()
    for n in line:
        numbers.append(int(n))

for i in range(1, 10):
    if i not in numbers:
        missing.append(i)

if not missing:
     print("This is a valid sudoku")
else:
    print("This is an invalid sudoku. Missing numbers are:")
    for m in missing:
        print(m)