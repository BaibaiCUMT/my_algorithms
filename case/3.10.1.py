from parcheck import parChecker
from fixtopost import infixToPostfix

def safeFixToPost(item):
    if parChecker(item):
        print(infixToPostfix(item))
    else:
        print('parentheses is not matched!')


print(safeFixToPost('(A+B)*(C+D)*(E+F))'))
