from testlist import list2


def quickSort(list):
    quickSortHelper(list, 0, len(list)-1)
    return list


def quickSortHelper(list, first, last):
    if first < last:
        
        splitpoint = partition(list,first,last)

        quickSortHelper(list, first, splitpoint-1)
        quickSortHelper(list, splitpoint+1, last)

def partition(list, first, last):
    pivotvalue = list[first]

    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        
        while leftmark <= rightmark and \
                    list[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while list[rightmark] >= pivotvalue and \
                    rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            list[leftmark],list[rightmark] =\
            list[rightmark],list[leftmark]

    list[first],list[rightmark] = list[rightmark],list[first]

    return rightmark


print(list2)
print(quickSort(list2))
