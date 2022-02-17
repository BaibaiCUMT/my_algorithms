def sequentialSearch1(list, item):
    for i in list:
        if i == 5:
            return True


def sequentialSearch2(list, item):
    pos = 0
    found = False

    while pos < len(list) and not found:
        if list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


alist = [i for i in range(1, 51, 2)]

print(sequentialSearch1(alist, 5))
print(sequentialSearch2(alist, 5))
print(5 in alist)