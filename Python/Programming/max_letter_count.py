'''
find the letter which occured the maxixmum times in a string.
'''

def max_letter(my_string: str) -> str:
    my_dict = {}
    
    #for getting count of each letter in a dict
    for i in range(len(my_string)):
        if my_string[i] not in my_dict:
            # my_dict[my_string[i]][0] = 1
            # my_dict[my_string[i]][1] = i
            my_dict[my_string[i]] = [1, i]
            #my_dict[my_string[i]][1] = i

        else:
            my_dict[my_string[i]][0] += 1
            

    print(my_dict)
            

    #now for comparing the count of each letter in that dict
    max_count = 0
    max_char = ""
    for key, value in my_dict.items():
        if value[0] > max_count:
            max_char = key
            max_count = value[0]
        elif value[0] == max_count:
            if value[1] < my_dict[max_char][1]:
                max_char = key
        
    return max_char

if __name__ == "__main__":
    print(max_letter("skhhhhkkjjjjKKKk"))

            


