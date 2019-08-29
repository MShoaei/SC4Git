count = 0
a = 2

def print_and_count(f):
    global count
    print("Hello", f())
    count += 1
