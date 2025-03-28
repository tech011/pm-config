def count_case(s):
    upper_count = 0
    lower_count = 0

    for ch in s:
        if 'A' <= ch <= 'Z':
            upper_count = upper_count + 1
        elif 'a' <= ch <= 'z':
            lower_count = lower_count + 1

    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

text = "Hello World!"
count_case(text)
