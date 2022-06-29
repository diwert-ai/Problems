def test0():
    items = []
    print(items)
    print(sorted(items, key=lambda x: items.count(x) - items.index(x)/len(items), reverse=True))
    

if __name__ == '__main__':
    test0()
   




