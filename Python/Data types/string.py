'''
properties and methods of a string
'''

#immutability: String is immutable

name = "joey"
# name[0] = 'P' : TypeError: 'str' object does not support item assignment

last_letters = name[1:]
print(last_letters)
new_name = 'P'+last_letters
print(new_name)

#multiply the number of letters
letter = 'z'
letter_10_times = letter * 10 
print(letter_10_times)

#string some of the built in methods
print(name.replace('j','k'))
print(name.split('e')) # ->  ['jo', 'y']
print(name.upper()) #name.lower() for lowercases

#string Interpolation / string formating
# .format() or f-strings (newer method)

print('My name is {}. My sisters name is {}'.format(name, new_name))

#f-strings method
print(f'My name is {name}. My sister is {new_name}')

print ('the {2} {0} {1}'.format('brown','fox','quick')) #the quick brown fox
#you can also assign them keywords instead of index
print('the {q} {b} {f}'.format(f='fox', q='quick', b='brown'))
print('the {q}{q}{q}'.format(f='fox', q='quick', b='brown')) # easy repetation the quickquickquick

result = 100/77
print(result) #1.2987012987012987
print("result is {r:2.3f}".format(r = result))


#Capitalize without using built in method


def capitalize_str(my_str: str):
    lower_str = my_str.lower()
    letters = list(lower_str)
    print(letters)
    letters[0] = letters[0].upper()
    new_str = "".join(letters)
    return new_str

def capitalise_str(my_str: str) -> str:
    return my_str[0].upper() + my_str[1:].lower()

def reverse_str(my_str : str) -> str:
    letters = list(my_str)
    i = 0
    j = len(letters) - 1
    while i < j:
        letters[i], letters[j] = letters[j], letters[i]
        i +=1
        j -=1

    return "".join(letters)


if __name__ == '__main__':
    # give_input = input("give input str: ")
    give_input = "saPNa"
    print(capitalize_str(give_input))
    print(capitalise_str(give_input))
    print(reverse_str(give_input))






