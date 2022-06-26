def test0():
    gamma = 0.96
    lr = 0.001

    for i in range(60):        
        print (i+1,lr)
        lr *= gamma

if __name__ == '__main__':
    test0()

