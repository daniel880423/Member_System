import numpy as np
def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    inf=float("inf")
    path=np.full((total,total), -1)  #列出路徑矩陣
    A=np.full((total,total), inf)   #列出A矩陣
    global road
    road=""

    for i in range(total): #對角線為0
        A[i][i]=0

    for i in matrix:   #將matrix路徑帶入
        A[i[0]-1][i[1]-1]=i[2]
                    
    for k in range(total): #找出最短路徑帶回A
        for i in range(total):
            for j in range(total):
                if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = k
                    
    def getpath(m,n): #遞迴尋找中斷點
        global road
        if path[m][n]!=-1:
            getpath(m,path[m][n])
            road+=str((path[m][n])+1)
            getpath(path[m][n],n)

    getpath(start-1,end-1)

    road=str(start)+str(road)+str(end)
    if A[start-1][end-1]==inf or A[start-1][end-1]==0:  #如果兩點間無路徑或為0
        road=None
        A[start-1][end-1]=-1
    
    return [int(A[start-1][end-1]),road]

if __name__ == '__main__':
    matrix = [[2, 1, 6], [2, 3, 8]]
    start = 2;end = 2; total =3
    print(homework_5(matrix, start, end, total))