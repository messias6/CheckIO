def check_io(numbers_array):
    return sorted(numbers_array,key=abs)

print(list(check_io((-20, -5, 10, 15))))