import numpy as np

def homework_5(matrix, start, end, total):
    lst = np.array([[9999 for _ in range(total)] for _ in range(total)])
    lst_= []
    for i in range(total):
        lst[i][i] = 0 
    
    for i in range(total ):
        lst[matrix[i][0] - 1][matrix[i][1] - 1] = matrix[i][2]
            
    print(lst)
    print('-'*50)
    
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if lst[i][j] > lst[i][k] + lst[k][j]:
                    lst[i][j] = lst[i][k] + lst[k][j]
                    if k+1 not in lst_:
                        lst_.append(k+1)
    
    lst_.append(end)
    lst_.insert(0, start)
    
    print(lst)
    print('-'*50)
    print('節點{}到節點{}的最短距離為{}'.format(start, end, lst[start - 1][end - 1]))
    print(lst_)

matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
start = 2
end = 4
total = 4
homework_5(matrix, start, end, total)