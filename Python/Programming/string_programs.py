"""
write a program to take input sentence from the user, replace the letters that are repeated into "&"

"""
#output = "The quick brown f&x j&mps &v&& &&& l&zy d&g."
def string_update(sentence):
    #my_str = sentence.replace(" ", "")
    my_set = set()
    result = ''
    for letter in sentence:
        if letter == " ":
            result += letter
            continue
        if letter not in my_set:
            my_set.add(letter)
            result += letter
        else:
            result += "&"
    return result

#sentence = 'The quick brown fox jumps quickly over the lazy brown dog.'
#output = 'The quick brown fox jumps quickly over &&& lazy &&&& dog'
def word_update(sentence: str):
    my_list = sentence.split(" ")
    my_set = set()
    new_list = []
    for item in my_list:
        if item.lower() not in my_set:
            my_set.add(item.lower())
            new_list.append(item)
        else:
            new_word = '&'*len(item)
            new_list.append(new_word)
    result = " ".join(new_list)
    return result

if __name__ == '__main__':
    #sentence = input("Please input a sentence")
    sentence = 'The quick brown fox jumps quickly over the lazy brown dog.'
    #print(string_update(sentence))
    print(word_update(sentence))


