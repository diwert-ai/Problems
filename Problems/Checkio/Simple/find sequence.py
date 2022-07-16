'''
https://py.checkio.org/ru/mission/find-sequence/

Дана квадратная матрица размера NxN (4≤N≤10). 
Необходимо проверить есть ли здесь последовательность 4 или более одинаковых цифр. 
Последовательность должна неразрывно располагаться горизонтально, вертикально или 
по диагоналям (основным и дополнительным).

Входные данные: Матрица, как список (list) списков с целыми числами.

Выходные данные: Есть ли здесь последовательность, как булево значение (bool).
'''

#мое решение: O(N^2) время О(N^2) память
from typing import List

def find_sequence(array:list):
    max_sequence_length = 0
    previous_element=array[0]
    for element in array:
        if element == previous_element:
            max_sequence_length +=1
            if max_sequence_length > 3:
                return True    
        else:
            max_sequence_length = 1
            previous_element = element
    return False
        

def checkio(matrix: List[List[int]]) -> bool:
    n = len(matrix)
    columns = [[row[i] for row in matrix] for i in range(n)]
    d0 = [[row[i+j] for i,row in enumerate(matrix) if i+j < n] for j in range(n-3)]
    d1 = [[row[i-j] for i,row in enumerate(matrix) if i-j > -1] for j in range(1,n-3)]
    d2 = [[row[-i+j-1] for i,row in enumerate(matrix) if -i+j-1 < 0] for j in range(n-3)]
    d3 = [[row[-i-j-1] for i,row in enumerate(matrix) if -i-j-1 > -n-1] for j in range(1,n-3)]
    diags = d0+d1+d2+d3
    
    for row in matrix:
        if find_sequence(row):
            return True
        
    for column in columns:
        if find_sequence(column):
            return True
        
    for diag in diags:
        if find_sequence(diag):
            return True
        
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1,2,3,4,5,6],
        [2,3,1,3,5,6],
        [1,2,1,2,3,4],
        [1,2,3,4,5,6],
        [2,3,8,7,5,4]
    ]) == False
    assert checkio([
        [1,2,3,4,5,6],
        [2,3,1,3,5,6],
        [1,0,0,0,0,4],
        [1,2,3,4,5,6],
        [2,3,8,7,5,4]
    ]) == True
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    print('All Done! Time to check!')