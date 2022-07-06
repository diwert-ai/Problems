#пример: бинарный поиск в отсортированном массиве
#из лекции  Хирьянова https://www.youtube.com/watch?v=EdhN_gEDfUM&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=10


def left_bound(array:list,key):
    left = -1
    right = len(array)

    while right - left > 1:
        middle = (left+right)//2
        if array[middle]<key:
            left = middle
        else:
            right = middle

    return left


def right_bound(array:list,key):
    left = -1
    right = len(array)

    while right - left > 1:
        middle = (left+right)//2
        if array[middle]<=key:
            left = middle
        else:
            right = middle

    return right

def test0():
    a = [1,12,2,4,6,6,7,8,9,6,4,3,21,12,34,5]
    a = sorted(a)

    keys = list(range(35))
    print(a)
    print(keys)

    for key in keys:
        l = left_bound(a,key)
        r = right_bound(a,key)
        print(key,a[l+1:r] if l > -2 and r <= len(a) and r-l>1 else 'not found!' )

if __name__ == '__main__':
    test0()


