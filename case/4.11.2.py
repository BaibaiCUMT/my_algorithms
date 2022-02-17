alist = [2, 6, 3, 9, 4, 12]


def reverse(list):
    if len(list) <= 1:
        return list
    else:
        return [list[-1]] + reverse(list[:-1])


print(reverse(alist))
