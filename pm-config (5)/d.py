word = "hello"
new_word = word[-1]  

for i in range(1, len(word)-1):
    new_word += word[i]  

new_word += word[0]  
print("Modified string:", new_word)
