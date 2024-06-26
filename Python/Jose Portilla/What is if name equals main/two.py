# two.py
import one

print('top level in Two.py')
one.func()

if __name__ == '__main__':
    print('two.py is run directly')
else:
    print('two.py is imported')