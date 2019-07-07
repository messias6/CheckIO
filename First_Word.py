def first_word(text: str) -> str:
    f = ''
    for l in text:
        if (l == ' '):
            return f
        else:
            f = f+l
    return f
print(first_word("Hello world"))
print(first_word("hi"))