#рекурсивный вывод слияния двух списков

def merge_print(a,b):
    if len(a) == 0:
        print(*b)
        return

    if len(b) == 0:
        print(*a)
        return

    if a[0]>b[0]:
        print(b[0],end=' ')
        merge_print(a,b[1:])
    else:
        print(a[0],end=' ')
        merge_print(a[1:],b)

    return

 
a=[1,2,3,5,6,7,8,8,8,10,100,400]
b=[-6,-5,4,5,5,5,5,5,5,6,6,6,6,7,700,800]

merge_print(a,b)
