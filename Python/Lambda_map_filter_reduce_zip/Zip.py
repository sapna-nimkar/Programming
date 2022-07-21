'''
combining two list/tuple in single entity
'''

products = ['a','b','c','d']
prices = [10,40,20,30]
weights = [88,55,33,21]

info = []
for i in range(len(products)):
    #details = [products[i], prices[i], weights[i]]
    info.append([products[i], prices[i], weights[i]])

#With Zip
info = list(zip(products, prices, weights))

