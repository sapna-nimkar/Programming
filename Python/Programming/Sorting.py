items = [10, 3, 8, 5, 1]

for i in range(len(items)-1):
    m = i
    for j in range(i+1, len(items)):
        if items[m] > items[j]:
            m=j
    items[i], items[m] = items[m], items[i]


print(items[0], items[len(items)-1])

