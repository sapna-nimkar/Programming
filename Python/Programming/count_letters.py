#count the letters in a given string


def join_mystr(my_str):
    new_str = my_str.split(" ") #will give me an array of all words in the string sentence
    print(new_str)
    newer_str = "".join(new_str)
    return newer_str.replace(".","")


def count_letters(my_str):
    letter_dict = {}
    for i in range(len(my_str)):
        result = my_str[i].lower()
        if result not in letter_dict.keys():
            letter_dict[result] = 1
        else:
            letter_dict[result] += 1

    return letter_dict
    

if __name__ == '__main__':
    my_str = 'My country is India. .'
    newer_str = join_mystr(my_str)
    print(type(newer_str))
    print(count_letters(my_str=newer_str))
