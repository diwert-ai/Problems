#пример: редакционное расстояние между строками (расстояние Левенштеина)
#из лекции Хирьянова https://www.youtube.com/watch?v=rEPggzaPoUw&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=12

#Рассмотрим 3 вида редакционных ошибок: 1) перепутали символ 2) вставили лишний символ 3) потеряли 
#нужный символ. Нужно найти наименьшее кол-во редакционных правок для превращения слова A в слово B 
#(редакционное расстояние между словами A и B).

#F_{i,j} - минимальное ред расстонияе между A[:i] и B[:j]
#если A[i-1] == B[j-1], то F_{i,j} = F_{i-1,j-1}
#если A[i-1] != B[j-1], то F_{i,j} = 1 + min (F_{i-1,j-1},F_{i-1,j},F_{i,j-1})
#F_{0,j}=j F_{i,0}=i F_{0,0}=0

def levenstein(A,B):
    N = len(A)+1
    M = len(B)+1
    F = [[i+j if i == 0 or j == 0 else 0 for j in range(M)] for i in range(N)]
    for i in range(1,N):
        for j in range(1,M):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i-1][j-1],F[i-1][j],F[i][j-1])

    return F,F[-1][-1]

def test0():
    a = 'молоко'
    b = 'колокол'
    print(levenstein(a,b))


if __name__ == '__main__':
    test0()


