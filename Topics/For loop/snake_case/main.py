word = input()
new_word = str("")

for char in word:
    if char.isupper():
        char = str("_" + char.lower())
    new_word = str(new_word + char)
print(new_word)
