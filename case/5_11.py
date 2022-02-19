from testlist import list2


def selectionSort(list):
    for fillslot in range(len(list)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if list[location] > list[positionOfMax]:
                positionOfMax = location

        list[fillslot],list[positionOfMax] =\
        list[positionOfMax],list[fillslot]
        print(list)
    return list


print(list2)
print('---------------------')
print(selectionSort(list2))
