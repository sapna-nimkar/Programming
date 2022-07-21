"""
Tuple is like list BUT 
Immutable/CANNOT change
Ordered
Duplicate YES

ROUND bracket
"""
my_tuple = (1,3,7)
single_tup = (2,)

# CANNOT append or add or anything
# Accessing the values of Tuple

this_tuple = ("apple","banana","cherry", "banana")

print(this_tuple[2]) # output: cherry

x = 1
print(this_tuple[x]) #outout : banana

#get number of items in a tuple

len(this_tuple) #output: 4

#TUPLE UNPACKING

stock_prices = [('APPL', 200), ('GOOG', 300), ('MIC', 100)]

for item in stock_prices:
    print(item)

#Unpacking the tuple
for ticker, price in stock_prices:
    print(ticker)
    print(price+(0.1*price))

#another way tuple unpacking via function
work_hours = [('Abby',100), ("Cloe", 2000), ('Ken', 400)]
#who has worked the most hour. return name plus hours worked

def eom_check(work_hours):
    current_max = 0
    winner = ''
    
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            winner = employee
        else:
            pass
        
    #Return
    return (winner,current_max)

print(eom_check(work_hours))
name,hours = eom_check(work_hours)
print(name)
print(hours)