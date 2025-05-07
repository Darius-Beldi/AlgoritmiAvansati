list =[(1,2) , (2,3), (3,4)]
list2 = [(1,2)]
list = set(x for x in list)
list2 = set(x for x in list2)
print(list - list2)