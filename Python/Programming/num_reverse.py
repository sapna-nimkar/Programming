'''
do the reverse of a number without using any other datatype
'''

def num_reverse(num:int):
    result = 0
    quo = num
    while quo >0:  
        reminder = quo%10
        result = result*10 + reminder
        quo = quo//10
    return result

print(num_reverse(523))
