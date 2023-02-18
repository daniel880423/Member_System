def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    if start == end:
        return [-1,None]
    infin = -1
    z = [infin]*total
    zz = [None]*total
    b=[]
    p = []
    for i in range(total):
        b.append(z[:])
    for i in range(total):
        p.append(zz[:])
    for i in range(total):
        b[i][i]=0
        p[i][i]=0
    for i in range(len(matrix)):
        b[matrix[i][0]-1][matrix[i][1]-1]= matrix[i][2]
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if b[i][k]==-1 or b[k][j] ==-1:
                    continue
                elif b[i][j]==-1:
                    b[i][j] = b[i][k]+b[k][j]
                    if p[i][k]!=None and p[k][j]==None:
                        p[i][j] = str(p[i][k])+str(k+1)
                    elif p[k][j]!=None and p[i][k]==None:
                        p[i][j] = str(k+1)+str(p[k][j])
                    elif p[k][j]!=None and p[i][k]!=None:
                         p[i][j] = str(p[i][k])+str(k+1)+str(p[k][j])
                    elif p[i][k]==None and p[k][j]==None:
                        p[i][j] = str(k+1)
                    continue
                else:
                    ggg = b[i][j]
                    b[i][j] = min(b[i][j],b[i][k]+b[k][j])
                    if ggg!=b[i][j] and p[i][k]!=None and p[k][j]==None:
                        p[i][j] = str(p[i][k])+str(k+1)
                    elif ggg!=b[i][j] and p[k][j]!=None and p[i][k]==None:
                        p[i][j] = str(k+1)+str(p[k][j])
                    elif ggg!=b[i][j] and p[k][j]!=None and p[i][k]!=None:
                         p[i][j] = str(p[i][k])+str(k+1)+str(p[k][j])
                    elif ggg!=b[i][j] and p[i][k]==None and p[k][j]==None:
                        p[i][j] = str(k+1)
    if b[start-1][end-1]==-1:
        anss = None
    else:
        anss = str(start)+str(p[start-1][end-1])+str(end)
    ans = [b[start-1][end-1],anss]
    return ans

if __name__ == '__main__':
    matrix = [[5, 1, 1], [5, 2, 2], [5, 3, 1], [5, 4, 2], [1, 5, 1], [4, 5, 2], [3, 5, 1], [2, 5, 2], [10, 1, 5], [10, 4, 6], [10, 2, 8], [3, 9, 2]]
    start = 10;end =9; total = 10
    print(homework_5(matrix, start, end, total))
    