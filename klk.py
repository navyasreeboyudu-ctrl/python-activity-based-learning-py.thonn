text = input("Enter a sentence: ")
words = text.lower().split()
for word in words:
    if words.count(word) > 1:
        print(word, "is repeated")

