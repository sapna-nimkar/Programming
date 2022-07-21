'''
List= Ordered sequences which can hold variety of object types

List Properties: 
ordered
mutable - can change , add, edit, update, delete
Duplicate YES
'''

#Creation
my_list = [1, "ABC", (2,3), 5.4, ["iAmNestedList", "we"], 2]
my_other_list = list((1, 'ABC', (3,5), ['x', 'y', 'z']))

"""
Accessing the list items
"""
#to get 1st item from the above list by index . Index will be number int always

my_list[0]

"""
index -1 referes to the last item of the list. -2 will be 2nd last item of the list
"""
# my_list[-2] will give me ["iAmNestedList", "we"]

"""
List Exceptions:
Index out of range
"""
l = []
try:
    l[0]
except IndexError as err:
    print(err)

#Functions/Methods

#Add/Insert Item at the end of the list

l = []
l.append(13)
 #Delete item from the end of the list

popped_item = l.pop()  #you can store the popped item into a variable and use it
print(popped_item)
print(l)

#Add item of one list into another

listA = [1,3,4]
listB = ['a','b']

listA.extend(listB)
print(listA) #output : [1,3,4,'a','b']

#same thing with concatenate operator but it will return a new list
listA + listB #output : newList = [1,3,4,'a','b']

listA.append(listB)
print(listA) #return [1,3,4,['a','b']]

# number of items in a list

len(listA) #output : 3

#List Comprehension






