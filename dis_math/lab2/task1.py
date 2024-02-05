word = "КОМБИНАТОРИКА"
words = []
for i in word:
    temp_word = i
    for j in word:
        temp_word = temp_word[:1] + j
        for k in word:
            temp_word = temp_word[:2] + k
            if not (temp_word in words):
                words.append(temp_word)

print(words)
print(len(words))
