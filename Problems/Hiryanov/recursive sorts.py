#пример рекурсивных сортировок 
#быстрая сортировка Тони Хоара - quick sort
#сортировка слияниями Джона фон Неймана - merge sort
#из лекции Хирьянова https://www.youtube.com/watch?v=2XFaK3bgT7w&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=8


def quick_sort(array:list):
    
    pass

def merge_sort(array:list):
    pass

def test(sort_algo):

    print(sort_algo.__doc__)

    tests = [[1,5,4,3,2,6,8,0,5,3],
             [1,1,1,1,2,2,2,3,3,3,4,4,4,4],
             [2,3,3,3,1,1,1,0,0,0,1,2,3,4],
             [-1,2,-1,2,-1,2,1,2,2,1],
             [0,0,0,0,0,0,0,0,0,0,0,-100],
             [10,11,22,33,44,0,1,2,3,4,5],
             [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4]]

    for num,test_unsorted in enumerate(tests):
        test_sorted = test_unsorted.copy()
        sort_algo(test_sorted)
        print(f"testcase #{num}: ","Ok!" if test_sorted == sorted(test_unsorted) else "Failed!")
        
    print('')

if __name__ == '__main__':
    for algo in [quick_sort,merge_sort]:
        test(algo)
