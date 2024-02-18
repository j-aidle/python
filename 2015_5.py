
def isPalindrome(s):
    return s == s[::-1]

results = []

while True:
    a = input()
    if a == 'Palindrome!':
        break

    if isPalindrome(a):
        results.append(f"\"{a}\" is a palindrome")
    else:
        results.append(f"\"{a}\" is not a palindrome")
        
for result in results:
    print(result)