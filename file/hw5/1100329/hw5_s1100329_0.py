def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path=[]
    A=[]
    name=[]
    pp=[]
    nnaa=''

    ## 創造矩陣 A 與 path
    for k in range(total):
        path.append([])
        A.append([])
        for j in range(total):
            path[k].append(-1)
            if k==j:
                A[k].append(0)
            else:
                A[k].append(float("inf"))
    for i in matrix :
        A[i[0]-1][i[1]-1]=i[2]

    # for i in A:   ##顯示路徑圖
    #     print(i)
    # print()
    
    for k in range (total):
        for i in range (total):
            for j in range (total):
                if (A[i][k]+A[k][j])<A[i][j]:
                    A[i][j]=min(A[i][j],(A[i][k] + A[k][j]))
                    path[i][j]=k
        # for i in path:   ##顯示路徑圖
        #     print(i)
        # print()
        # for i in A:   ##顯示A矩陣
        #     print(i)
        # print()



    def getpath(i,j,path,nn):
        if (path[i][j]!=-1):
            getpath(i,path[i][j],path,nn)
            #print(path[i][j]+1)
            nn.append(str(path[i][j]+1))
            getpath(path[i][j],j,path,nn)
    
    getpath(start-1,end-1,path,name)

    if A[start-1][end-1]==float("inf"):
        return [-1,None]

    # for i in A:
    #     print(i)
    # print()
    # for i in path:
    #     print(i)
    for i in name:
        nnaa=nnaa+str(i)
    #print(A[start-1][end-1])
    pp.append( A[start-1][end-1])
    pp.append(str(start)+nnaa+str(end))
    return pp

if __name__ == '__main__':
    matrix = [[1, 2, 1], [1, 3, 3], [2, 1, 2], [3, 4, 4]]
    start = 2;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    