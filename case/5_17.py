from testlist import list2


def insertionSort(list):
    for position in range(1,len(list)):
        
        currentvalue = list[position]

        while position > 0 and list[position-1] > currentvalue:
            list[position] = list[position-1]
            position = position - 1

        list[position] = currentvalue
    return list


print(list2)
print(insertionSort(list2))
