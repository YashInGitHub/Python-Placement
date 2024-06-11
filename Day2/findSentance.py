givenString = str(input())

wordCount = 0
numberCount = 0
upperWordCount = 0
lowerWordCount = 0

for c in givenString:
    if c.isalpha():
        wordCount += 1
    if c.isdigit():
        numberCount += 1
    if c.isupper():
        upperWordCount += 1
    if c.islower():
        lowerWordCount += 1

print("Number of words: ", wordCount)
print("Number of numbers: ", numberCount)
print("Number of uppercase words: ", upperWordCount)
print("Number of lowercase words: ", lowerWordCount)