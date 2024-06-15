import string
sentence = input("Enter a sentence: ")
wordList = sentence.strip().split(" ")
print(f"This sentence has {len(wordList)} words")

digitCount = 0
lowerCaseCount = 0
upperCaseCount = 0

for char in sentence:
    if char in string.digits:
        digitCount+=1
    elif char in string.ascii_lowercase:
        lowerCaseCount+=1
    elif char in string.ascii_uppercase:
        upperCaseCount+=1

print(f"This sentence has {digitCount} digits")
print(f"This sentence has {lowerCaseCount} lowercase letters")
print(f"This sentence has {upperCaseCount} uppercase letters")

