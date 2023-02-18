import numpy as np


def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    
    path=np.zeros((total,total),dtype=int)
    A=np.zeros((total,total))
    inf=float("inf")
    road=""
    #for i in range(1,n+1):
        #for j in range(1,n+1):
            #path[i][j]=-1
    for i in range(0, total):
	    for j in range(0, total):
		    path[i][j]=-1

    for i in matrix:
        A[i[0]-1][i[1]-1]=i[2]
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i==j:
                A[i][i]=0
            elif (A[i][j]==0):
                A[i][j]=inf

    for k in range(0, total):
        for i in range(0, total):
            for j in range(0, total):
                if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
                    path[i][j] = k+1
                    
    
    while(path[start-1][end-1]!=-1):
        x=path[start-1][end-1]
        
        road=str(path[start-1][end-1])+road
        path[start-1][end-1]=path[start-1][x-1]


    while(path[x-1][end-1]!=-1):
        y=path[x-1][end-1]
        if (path[x-1][y-1]!=-1):
            road=road+str(path[x-1][y-1])
            k=path[x-1][y-1]
            path[x-1][y-1]=path[x-1][k-1]
        road=road+str(path[x-1][end-1])
        path[x-1][end-1]=path[x-1][y-1]


        


    road=str(start)+road

    if (road[-1]!=str(end)):
        road=road+str(end)

    if(A[start-1][end-1]==inf):
        return [-1,None]
    if(A[start-1][end-1]==0):
        return [-1,None]

    return [int(A[start-1][end-1]),road]

if __name__ == '__main__':
    matrix = [[1, 2, 4], [1, 3, 5], [2, 6, 1], [3, 4, 4], [3, 1, 1], [4, 5, 2], [5, 6, 6], [6, 7, 10], [4, 3, 1]]
    start = 4;end = 6; total =7
    print(homework_5(matrix, start, end, total))
    
    