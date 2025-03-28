def is_palindrome(s):
    rev = ""  
    for i in range(len(s)-1, -1, -1):  
        rev = rev + s[i]  
    return s == rev  

word = "madam"
print("Is palindrome:", is_palindrome(word))
