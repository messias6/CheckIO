def check_io(*args):
    return (max(args, default=0)-min(args, default=0))

print(check_io(1,2,3))
print(check_io())