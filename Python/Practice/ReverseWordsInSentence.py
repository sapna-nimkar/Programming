sentence = 'Sapna can do anything'

def reverse_letters(sentence):

    #separate words from sentence

    sen_list = sentence.split(" ")

    #reverse words
    words = []
    for item in sen_list:
        words.append(reverse_word(item))
    
    result = " ".join(words)
    return result

   #join words to sentence in same order

def reverse_word(word: str)-> str:

    letters = list(word)
    i = 0
    j = len(letters)-1
    while i < j:
        letters[i], letters[j] = letters[j], letters[i]
        i += 1
        j -= 1
    word = "".join(letters)
    
    return word


# print(reverse_letters(sentence))

k = 13
items =[8, 4, 6, 3, 1, 2, 10, 7, 9]

def two_sum(items, k):
    result = []
    for i in range(len(items) - 1):
        for j in range(i+1, len(items)):
            if items[i] + items[j] == k:
                result.append((items[i], items[j]))
    return result

print(two_sum(items, k))

def two_sum_optimise(items, k):
    result_unique = set()
    unique_items = set(items)
    for i in range(len(items) - 1):
        if k - items[i] in unique_items:
            # result.append((items[i], k - items[i]))
            if items[i] <  k - items[i]:
                result_unique.add((items[i], k - items[i]))
            else:
                result_unique.add((k - items[i], items[i]))
    return list(result_unique)

print(two_sum_optimise(items, k))


#sort a list without in-built method

data = [10,3,8,2,1,10,2,6]

def sort_list(data: list):

    for i in range(len(data)-1):
        minimum_idx = i
        for j in range(i+1,len(data)):
            if data[j] < data[minimum_idx]:
                minimum_idx = j
        data[i], data[minimum_idx] = data[minimum_idx], data[i]
            

sort_list(data)
print(data)


# data = [10,3,8,2,10,2,6]
#         m
#            i
# new_data = [1]
# def sort_while(data):
#     new_data = []
#     while len(data):
#         min_idx = 0
#         for i in range(len(data)):
#             if data[i] < data[min_idx]:
#                 min_idx = i
        
#         new_data.append(data[min_idx])
#         data.pop(min_idx)
#     return new_data

# print(sort_while(data))





