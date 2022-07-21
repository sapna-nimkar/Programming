'''
check two words are anagram of each other
'''

def is_anagram(word_a, word_b):
    if len(word_a) != len(word_b):
        return False
    counter_a = {}
    counter_b = {}

    for i in word_a:
        if i not in counter_a:
            counter_a[i] = 1
        else:
            counter_a[i] += 1

    for j in word_b:
        if j not in counter_b:
            counter_b[j] = 1
        else:
            counter_b[j] += 1

    for key, value in counter_a.items():
        if key not in counter_b or value != counter_b[key]:
            return False
    return True


    #return counter_a == counter_b

if __name__ == '__main__':
    word_a = 'iamlordvoldemort'
    word_b = 'tommarvoloriddle'
    print(is_anagram(word_a, word_b))
