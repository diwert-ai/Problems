def test0():
    l = ['a','b','bb','bb']
    cnt = 0
    item = ''
    for i in l:
        n_cnt = l.count(i)
        if n_cnt > cnt:
            cnt = n_cnt
            item = i

    return item

def test1():
    l = ['a','b','bb','bb']

    return max(set(l), key = l.count)




if __name__ == '__main__':
    print(test1())
        

