def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    return text.replace('.', ' ').replace(',', ' ').split()[0]

print(first_word(" a word "))
