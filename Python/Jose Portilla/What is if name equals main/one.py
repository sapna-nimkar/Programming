# one.py

def func():
    print("some func() in one.py")
print("TOP level in one.py i.e indent 0")

if __name__ == '__main__':
    print("One.py was run directly by python")
else:
    print("one.py has been imported")