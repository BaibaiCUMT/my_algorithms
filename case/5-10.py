from testlist import list2

def shortBubbleSort(list):
    exchange = True
    passnum = len(list) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if list[i] > list[i+1]:
                exchange = True
                list[i],list[i+1] = list[i+1],list[i]
        passnum = passnum - 1
    return list


#    for passnum in range(len(list)-1,0,-1):
#        for i in range(passnum):
#            if list[i] > list[i+1]:
#                list[i],list[i+1] = list[i+1],list[i]
#    return list

print(list2)
print(shortBubbleSort(list2))
