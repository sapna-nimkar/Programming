'''
this is the program to turn uppercase letters to lowercae and vice versa
'''
#using a new string

def upper_lower(my_str):
    new_str = ""
    for letter in my_str:
        if letter == letter.upper():
            letter = letter.lower()
            new_str = new_str+letter
        elif letter == letter.lower():
            letter = letter.upper()
            new_str = new_str+letter
    print(new_str)

    return new_str

#using list

def lower_upper(my_str):
    my_list = list(my_str)
    for i in range(len(my_list)):
        if my_list[i] == my_list[i].upper():
            my_list[i] = my_list[i].lower()

        elif my_list[i] == my_list[i].lower():
            my_list[i] = my_list[i].upper()

    new_str = ''.join(my_list)
    return new_str

            

if __name__ == '__main__':
    my_str = 'dYUaqR'
    print(upper_lower(my_str))
    print(lower_upper(my_str))