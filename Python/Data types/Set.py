"""
UNORDERED COLLECTION OF UNIQUE ELEMENTS
NOT ordered
Mutable - can add or remove value
Unindexed
"""
# YOU can Remove or ADD items in sets but NOT change/update

myset = {1,5,4,22,4,4,4}

myset.remove(5)
print(myset)
myset.add(9)
print(myset)
print(len(myset))





#perform set operations (mathematical sets union, intersection, difference, symmetric difference)

A = {1,2,3}
B = {4,2, 1,6,7,88,4,6}
print(B)
print(B.union(A))
print(A | B)
print(A.intersection(B))
print(A&B)
print(A.difference(B))
print(A-B)
print(B.difference(A))
print(B-A)

#symmetric difference = items in ONLY A and in ONLY B. excluding the intersection common items
print(A^B)
print(A.symmetric_difference(B))

#check if element present in set

a = set("apple")
print(a)
#if 'p' in a:
    #print("{} is present in {}".format('p',a))
if 'q' not in a:
    print('q is not present in {}'.format(a))
    print('q' not in a)

#we can Iterate through a set
for letter in set("banana"):
    print(letter)

#enumerate assigns a value to the set elements
apple = {'o','r','a','n','g','e','g','e','o'}
print(dict(enumerate(apple)))
 

