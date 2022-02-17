alist = [1,3,2,4,5,6]

def reverseList(list):
    if len(list) <= 1:
        return list
    else:
        return [list[-1]] + reverseList(list[:-1])

print(reverseList(alist))