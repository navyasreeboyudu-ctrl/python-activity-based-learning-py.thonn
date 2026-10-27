text = input("Enter text: ")
encoded = ""
i = 0
while i < len(text):
    count = 1
    while i + 1 < len(text) and text[i] == text[i + 1]:
        count = count + 1
        i = i + 1
    encoded = encoded + text[i] + str(count)
    i = i + 1
print("Encoded text:", encoded)
if len(encoded) < len(text):
    print("Encoding saves space.")
else:
    print("Encoding does not save space.")

