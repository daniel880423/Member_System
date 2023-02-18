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
        

    road=str(start)+road

    if (road[-1]!=str(end)):
        road=road+str(end)

    if(A[start-1][end-1]==inf):
        return [-1,None]
    if(A[start-1][end-1]==0):
        return [-1,None]

    return [int(A[start-1][end-1]),road]

if __name__ == '__main__':
    matrix = [[2, 1, 6], [2, 3, 8]]
    start = 2;end = 2; total =3
    print(homework_5(matrix, start, end, total))
    
    