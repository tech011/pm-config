def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    found = [0] * 26  

    for ch in s:
        if 'a' <= ch <= 'z':
            found[ord(ch) - ord('a')] = 1
        elif 'A' <= ch <= 'Z':
            found[ord(ch) - ord('A')] = 1

    for i in range(26):
        if found[i] == 0:
            return False
    return True

text = "The quick brown fox jumps over the lazy dog"
print("Is pangram:", is_pangram(text))
