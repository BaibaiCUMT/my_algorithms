from testlist import list2


def shellSort(list):
    sublistcount = len(list) // 2
    print(sublistcount)
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(list,startposition,sublistcount)

        print('After increments of size',sublistcount,
        'the list is\n',list)

        sublistcount = sublistcount // 2


def gapInsertionSort(list,start, gap):
   # print(list,start,gap)
    for i in range(start+gap, len(list), gap):

        currentvalue = list[i]
        position = i

        while position >= gap and \
                        list[position-gap] > currentvalue:
            list[position] = list[position-gap]
            position = position - gap

        list[position] = currentvalue


print(list2)
print(shellSort(list2))
