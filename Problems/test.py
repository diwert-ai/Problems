V = {'A','B','C','D'} # размер V (кол-во вершин) = N порядок графа
E = { ('A','B'), ('B','C'), ('C','D')} #размер E (кол-во  ребер) = M размер графа

#проверка на смежность двух вершин требует O(1) времени 
for i in V:
    for j in V:
        if i!=j:
            print(f'{(i,j)} is edge') if (i,j) in E or (j,i) in E else print(f'{(i,j)} is not edge')

#в такой структуре данных поиск всех соседних вершин требует О(N) времени
def get_neighbors(v):
    print(f'find neigbors of {v}...')
    for i in V:
        if (v,i) in E or (i,v) in E:
            print(f'{i} is neighbor {v}')


get_neighbors('B')

#матрица смежности

