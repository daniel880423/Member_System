def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    if start == end:
        return [-1,None]
    aa = -1
    d = [aa]*total
    dd = [None]*total
    a=[]
    p = []
    for i in range(total):
        a.append(d[:])
    for i in range(total):
        p.append(dd[:])
    for i in range(total):
        a[i][i]=0
        p[i][i]=0
    for i in range(len(matrix)):
        a[matrix[i][0]-1][matrix[i][1]-1]= matrix[i][2]
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if a[i][k]==-1 or a[k][j] ==-1:
                    continue
                elif a[i][j]==-1:
                    a[i][j] = a[i][k]+a[k][j]
                    if aaa!=a[i][j] and p[i][k]!=None:
                        p[i][j] = str(p[i][k])+str(k+1)
                    elif aaa!=a[i][j] and p[k][j]!=None:
                        p[i][j] = str(k+1)+str(p[k][j])
                    elif aaa!=a[i][j] and p[i][k]!=None and p[k][j]!=None:
                        p[i][j] = str(p[i][k])+str(k+1)+str(p[k][j])
                    elif aaa!=a[i][j] and p[i][k]==None and p[k][j]==None:
                        p[i][j] = str(k+1)
                    continue
                else:
                    aaa = a[i][j]
                    a[i][j] = min(a[i][j],a[i][k]+a[k][j])
                    if aaa!=a[i][j] and p[i][k]!=None:
                        p[i][j] = str(p[i][k])+str(k+1)
                    elif aaa!=a[i][j] and p[k][j]!=None:
                        p[i][j] = str(k+1)+str(p[k][j])
                    elif aaa!=a[i][j] and p[i][k]!=None and p[k][j]!=None:
                        p[i][j] = str(p[i][k])+str(k+1)+str(p[k][j])
                    elif aaa!=a[i][j] and p[i][k]==None and p[k][j]==None:
                        p[i][j] = str(k+1)
    if a[start-1][end-1]==-1:
        anns = None
    else:
        anns = str(start)+str(p[start-1][end-1])+str(end)
    ans = [a[start-1][end-1],anns]
    return ans

if __name__ == '__main__':
    matrix = [[5, 1, 1], [5, 2, 2], [5, 3, 1], [5, 4, 2], [1, 5, 1], [4, 5, 2], [3, 5, 1], [2, 5, 2], [10, 1, 5], [10, 4, 6], [10, 2, 8], [3, 9, 2]]
    start = 10;end =9; total = 10
    print(homework_5(matrix, start, end, total))
    