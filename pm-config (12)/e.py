words = ["apple", "banana", "strawberry", "kiwi"]
max_length = 0  

for word in words:
    count = 0  
    for ch in word:
        count = count + 1  
    if count > max_length:
        max_length = count  

print("Length of longest word:", max_length)
