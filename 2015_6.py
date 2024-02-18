word = ""
vowels = 0
consonants = 0
ratio = 0.0
end = False

while not end:
    word = input().lower()
    for x in range(len(word)):
        character = word[x]
        if (character in ['a', 'e', 'i', 'o', 'u']):
            vowels += 1
        elif ('a' <= character <= 'z'):
            consonants += 1
        if character == '#':
            end = True

    if not end:
        continue 

ratio = vowels / consonants if consonants != 0 else float('inf')

# Results
print("Consonants:", consonants)
print("Vowels:", vowels)
if consonants == 0:
    print("Ratio: Infinite")
else:
    print("Ratio: {:.3f}".format(ratio))
