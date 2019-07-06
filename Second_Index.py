def second_index(text, symbol):
    part = text.split(symbol,2)
    if len(part) <= 2:
        return None
    # y = length of input string - length of what is left
    # after the second split - length of what we wanted to find
    y = len(text) - len(part[-1]) - len(symbol)
    return y


print(second_index("sims", "s"))
print(second_index("find the river", "e"))
print(second_index("hi", " "))
print(second_index("hi mayor", " "))
print(second_index("hi mr Mayor", " "))
