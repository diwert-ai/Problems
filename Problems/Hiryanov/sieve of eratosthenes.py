#задача решето эратосфена из лекции Хирьянова
#https://www.youtube.com/watch?v=3I6OjxoeSS8&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=5



def sieve_of_eratocthenes(N:int):
    A = [True] * N
    A[0] = A[1] = False

    for k in range(2,N):
        if A[k]:
            for m in range(2*k,N,k):
                A[m] = False

    for k in range(N):
        print(k,A[k])


if __name__ == '__main__':
    sieve_of_eratocthenes(100)