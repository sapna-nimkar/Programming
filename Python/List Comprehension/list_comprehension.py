'''
used to CREATE a list or any other non-primitive dfata type based on iteration and certain conditions
'''

#Create a list of 10 numbers using list comprehension

#without
my_list = []
for i in range(10):
    my_list.append(i)

#With List Comp
my_list = [i for i in range(10)]

#already have some list eg. my_list above
# create a new list which will only contain Cube of ODD numbers from my_list
new_list = []
for item in my_list:
    if item%2 != 0:
        new_list.append(item**3)

#WITH LIST COMP

new_list = [item**3 for item in my_list if item%2 != 0]

#SET Comprehension

new_set = {item**3 for item in my_list if item%2 != 0}

#Dictionary Comprehension
my_dict = {'Joey': 200, 'Jenny': 300, 'Bhalu': 500}

new_dict = {}

for key,value in my_dict.items():
    if value < 500:
        bonus = value *0.10
        new_dict[key] = bonus

#using dict comp

new_dict = {key:value*0.10 for key,value in my_dict.items() if value<500}



