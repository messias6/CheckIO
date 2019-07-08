def check_io(words: str) -> bool:
    i=0
    for word in words.split():
        if word.isalpha():
            i+=1
        else:
            i=0
        if i==3:
            return True
    return False

print(check_io("Hello World hello"))
print(check_io("He is 123 man"))