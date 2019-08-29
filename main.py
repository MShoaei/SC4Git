count = 0

def print_and_count(f):
    global count
    print("Hello", f())
    count += 1
