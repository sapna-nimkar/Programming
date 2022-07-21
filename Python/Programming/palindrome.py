#check if a word is palindrome or not

def is_palindrome(word):
    i = 0
    j = len(word)-1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == "__main__":
    word = 'amma'
    print(is_palindrome(word))