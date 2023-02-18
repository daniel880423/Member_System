import numpy as np
def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path=np.zeros((total,total),dtype=int)  #列出路徑矩陣
    A=np.zeros((total,total))   #列出A矩陣
    inf=float("inf")
    global road
    road=""
    for i in range(0, total):      #將矩陣皆設為-1
	    for j in range(0, total):
		    path[i][j]=-1
    
    for i in range(0, total):  #將矩陣皆設為無限大
	    for j in range(0, total):
		    A[i][j]=inf   
    
    
    for i in range(0,total):  #對角線為0
        for j in range(0,total):
            if i==j:
                A[i][i]=0
    for i in matrix:   #將matrix路徑帶入
        A[i[0]-1][i[1]-1]=i[2]
            
            
    
                    
    for k in range(0,total): #找出最短路徑帶回A
        for i in range(0, total):
            for j in range(0, total):
                if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
                    path[i][j] = k
                    
    def getpath(m,n): #遞迴尋找中斷點
        global road
        if path[m][n]!=-1:
            getpath(m,path[m][n])
            road+=str((path[m][n])+1)
            getpath(path[m][n],n)

    getpath(start-1,end-1)

    road=str(start)+str(road)+str(end)
    if A[start-1][end-1]==inf: #如果兩點間無路徑
        road=None
        A[start-1][end-1]=-1
    
    return [int(A[start-1][end-1]),road]

if __name__ == '__main__':
    matrix = [[1, 2, 4], [1, 3, 5], [2, 6, 1], [3, 4, 4], [3, 1, 1], [4, 5, 2], [5, 6, 1], [6, 7, 10]]
    start = 3;end = 6; total =8
    print(homework_5(matrix, start, end, total))