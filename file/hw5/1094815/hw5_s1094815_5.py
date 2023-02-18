def homework_5(matrix, start, end, total): 
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path=[[-1]*total for c in range(total)]
    A=[[float('inf')]*total for a in range(total)]
    for i in range(total):
        A[i][i]=0
    for d in range(len(matrix)):
        p=matrix[d][0]-1
        q=matrix[d][1]-1
        A[p][q]=matrix[d][2]
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if (A[i][k]+A[k][j]<A[i][j]):
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
                    path[i][j]=k+1

    out1=A[start-1][end-1]
    fin=path[start-1][end-1]
    out2=str(end)
    while fin!=-1:
        out2+=str(fin)
        fin=path[start-1][fin-1]
    out2+=str(start)   
    out2 = "".join(reversed(out2))
    if len(out2)==2:
        out2=None
        out1=-1
    return [out1,out2]

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]] 
    start = 2;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    