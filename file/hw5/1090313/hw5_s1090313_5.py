def homework_5(matrix, start, end, total): 
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。

    #totle = n
    path = [[-1]*total for i in range(total)]
    A = [[float("inf")]*total for i in range(total)]
    for i in range(total):
        A[i][i]=0

    for i in matrix:
        A[i[0]-1][i[1]-1]=i[2]

    for k in range(0,total):
        for i in range(0,total):
            for j in range(0,total):
                if A[i][k]+A[k][j]<A[i][j]:
                    A[i][j] = min(A[i][k]+A[k][j],A[i][j])
                    path[i][j] = k
    
    if A[start-1][end-1]!=float("inf"):
        ans=[A[start-1][end-1]]+[str(start)+""]
        get_path(path,start,end,ans)
        ans[1]+=str(end)
    else:
        ans=[-1,None]
    return ans

def get_path(p,st,en,ans):
    if p[st-1][en-1]!=-1:
        #ans[1]+=str(p[st-1][en-1]+1)
        get_path(p,st,p[st-1][en-1]+1,ans)
        ans[1]+=str(p[st-1][en-1]+1)


if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2;end = 3; total = 4
    print(homework_5(matrix, start, end, total))
    hw5_In = [
    [[[1,2,1],[1,3,1],[3,4,1]], 1, 4, 4],
    [[[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]], 2, 5, 5],
    [[[1,2,1],[1,3,3],[2,1,2],[3,4,4]], 2, 4, 4],
    [[[1,2,1],[1,3,3],[2,1,2],[3,4,4]], 2, 3, 4],
    ]
    