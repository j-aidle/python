def isVowel(c):
    c = c.lower()
    if (c == "a" or c == "e" or c == "i" or c == "o" or c == "u"):
        return True
    else:
        return False


word = input()
outputWord = word
# Main program
for i in range(len(word)-1):
    # Look for a candidate pair of vowels in the word
    if (isVowel(word[i]) and isVowel(word[i+1])):
        # Check that there are no vowels before or after
        if (i-1 >= 0):
            if (isVowel(word[i-1])):
                # Found a vowel before, so discard this pair and continue the search
                continue
        if (i+2 <= len(word)-1):
            if (isVowel(word[i+2])):
                #    Found a vowel after, so discard this pair and continue the search
                continue
# This is a real pair of vowels swap them
        outputWord = outputWord[:i] + word[i+1] + word[i] + outputWord[i+2:]
print(outputWord)
