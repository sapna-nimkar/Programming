"""
Unordered Mappings for storing objects. Key Value pair. Quickly grab the objects without index location ss
Mutable
NOT Duplicate -> KEY cannot be duplicate , values can be duplicate
"""
my_dict = {'a': 1, 'b': 2, 'c': 5}

other_way = dict(a=2, b =8, c= 3)

#Accessing the dictionary items

my_dict.get('c')
my_dict['c']
x = my_dict.keys() #will return list of keys
y = my_dict.values() #will return list of values in the dictionary

#Changing / updating values in the dictionary

my_dict['b'] = 100 #will set the value of key 'b' as 100
other_way.update({'a': 200})
other_way.update({'zey': 6})

#Adding item (key and value) to dictionary
my_dict['s'] = 'sup'

#Remove Item from Dictionary
my_dict.pop('a') #will remove key a and value of key a from dict

#Remove Last Item from Dict
my_dict.popitem()

#Delete
del my_dict['b']

del my_dict #will delete the whole dictionary

#Empty the dictionary
my_dict.clear() #will empty the dictionary and simply return {}






