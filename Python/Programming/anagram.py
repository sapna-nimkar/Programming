#check if two words are anagram of each other or not

def is_anagram(worda, wordb):
    if len(worda) != len(wordb):
        return False
    counter_worda = {}
    counter_wordb = {}
    for letter in worda:
        if letter not in counter_worda:
            counter_worda[letter] = 1
        else:
            counter_worda[letter] += 1
    for letter in wordb:
        if letter not in counter_wordb:
            counter_wordb[letter] = 1
        else:
            counter_wordb[letter] += 1
    #compare the count of two dicts
    
    for key,value in counter_worda.items():
        if counter_wordb[key] != value:
            return False
    return True  #here we have missed test case where Key is not present in counter_wordb : will give KeyError and stop the program

if __name__ == '__main__':
    worda = 'iamlordvoldemort'
    wordb = 'tommarvoloriddle'
    print(is_anagram(worda, wordb))
