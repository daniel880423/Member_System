# 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
def path(p,start,end):
    global ans
    if start>=0 and end>=0:
        if p[start][end]>=0 :
            path(p,start,p[start][end])
            ans = ans + str(p[start][end]+1)
            path(p,p[start][end],end)
    
        
def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    if start == end:
        return [-1,None]
    aa = -1
    d = [aa]*total
    a=[]
    p = []
    for i in range(total):
        a.append(d[:])
        p.append(d[:])
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
                    p[i][j] = k
                else:
                    aaa = a[i][j]
                    a[i][j] = min(a[i][j],a[i][k]+a[k][j])
                    if aaa!=a[i][j]:
                        p[i][j] = k
    global ans 
    if p[start-1][end-1]!=aa:
        ans = str(start)
        anss = path(p,start-1,end-1)
        anss = ans + str(end)
    else:
        return [-1,None]
    return [a[start-1][end-1],anss]

if __name__ == '__main__':
    matrix = [[1, 2, 1], [1, 3, 3], [2, 1, 2], [3, 4, 4]]
    start = 2;end =3; total = 4
    print(homework_5(matrix, start, end, total))
    