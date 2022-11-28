class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l  = l
        self.r = r

def post_order(tree):
    if tree == None:
        return
    post_order(tree.l)
    post_order(tree.r)
    print (tree.v)

def in_order(tree):
    if tree == None:
        return
    in_order(tree.l)
    print (tree.v)
    in_order(tree.r)

def pre_order(tree):
    if tree == None:
        return
    print(tree.v)
    post_order(tree.l)
    post_order(tree.r)


def get_number(arr):
        if check(arr, '('):
            x = sum(arr)
            check(arr, ')')
            return x
        else:
            x = arr[0]
            if type(x) != type(0): return None
            arr[0:1] = []
            return Node(x, None, None)

def sum(arr):
        a = comp(arr)
        if check(arr, '+'):
            b = sum(arr)
            return Node('+', a, b)
        else:
            return a

def comp(arr):
        a = dif(arr)
        if check(arr, '*'):
            b = comp(arr)
            return Node('*', a, b)
        else:
            return a


def dif(arr):
    a = div(arr)
    if check(arr, '-'):
        b = comp(arr)
        return Node('-', a, b)
    else:
        return a

def div(arr):
    a = get_number(arr)
    if check(arr, '/'):
        b = comp(arr)
        return Node('/', a, b)
    else:
        return a

def check(arr, s):
        if arr[0] == s:
            del arr[0]
            return True
        else:
            return False


arr = [18,'*','(',13,'-',3,')','*',4,'/','(',10,'-',2,')', 'end']
tree = sum(arr)
print('Постфикс: ')
post_order(tree)
print('\n')
print('Инфикс: ')
in_order(tree)
print('\n')
print('Префикс: ')
pre_order(tree)
