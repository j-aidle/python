# Read input as string
value = str(input())

if value.isdigit():
    # Converting from number to base-26
    number = int(value)
    string = ""
    
    while number > 0:
        remainder = (number - 1) % 26
        number = (number - 1) // 26
        string = chr(65 + remainder) + string

    print(string)
else:
    # Converting from base-26 to number
    string = value.upper()
    value = 0
    power = 0

    # String is reversed to simplify how the traverse is done, increasing the power digit after digit
    for i in reversed(string):
        value = (ord(i) - 64) + value * 26
        power += 1

    print(str(value))
    