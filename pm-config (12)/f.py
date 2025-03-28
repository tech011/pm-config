word = "play"
word_new = ""

if not (word[-3:] == "ing"):
    word_new = word
    word_new = word_new + "i"
    word_new = word_new + "n"
    word_new = word_new + "g"
else:
    word_new = word

print("Modified string:", word_new)
