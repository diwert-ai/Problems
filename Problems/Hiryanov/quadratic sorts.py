#квадратичные сортировки O(N^2). сортировка вставками - insert sort, 
#сортировка выбором - choise sort, сортировка "пузырьком"
#из лекции Хирьянова https://www.youtube.com/watch?v=NLq7nB9bV0M&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=6

def insert_sort(array:list):
    '''алгоритм сортировки вставками - insert sort'''

    for k in range(1,len(array)):
        #фиксируем индекс элемента, который хотим вставить 
        j = k
        
        #осуществляем вставку элемента в часть массива, которая уже отсортирована
        while j > 0 and array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
            j -= 1

def choise_sort(array:list):
    '''алгоритм сортировки выбором - choise sort'''
 
    for k in range(len(array)-1):
        for j in range(k+1,len(array)):
            if array[j] < array[k]:
                 array[k],array[j] = array[j],array[k]

def bubble_sort(array:list):
    '''алгоритм сортировки "пузырьком" - bubble sort'''

    for k in range(len(array)-1):
        for j in range(len(array)-k-1):
            if array[j] > array[j+1]:
                array[j+1],array[j] = array[j],array[j+1]

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
    for algo in [insert_sort,choise_sort,bubble_sort]:
        test(algo)
    

