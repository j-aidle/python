def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

results = []

while True:
    a = int(input())
    
    if a == 0:
        break

    if is_prime(a):
        results.append(f"{a} is prime")
    else:
        results.append(f"{a} is not prime")

for result in results:
    print(result)