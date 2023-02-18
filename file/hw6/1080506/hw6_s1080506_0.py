def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    inf = float('Inf')
    A = [[inf]*total for i in range(total)] #存取路徑
    P = [[-1]*total for i in range(total)] #存取中轉點
    lst = []
    route = str(start)
    for i in range(len(matrix)):
        A[matrix[i][0]-1][matrix[i][1]-1] = matrix[i][2]  #將matrix點到點的路徑更新到A矩陣
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if A[i][j] > A[i][k]+A[k][j]:
                    A[i][j] = min(A[i][j],A[i][k]+A[k][j])
                    P[i][j] = k
    if A[start-1][end-1]!=inf:
        lst.append(A[start-1][end-1])
        lst.append(route)
        getroute(start-1,end-1,P,route,lst)
        lst[1]=lst[1]+str(end)
    else:
        lst=[-1,None]
    return lst
def getroute(i,j,P,route,lst):
    if P[i][j]!=-1:
        getroute(i,P[i][j],P,route,lst)
        lst[1] = lst[1]+str(P[i][j]+1)
        getroute(P[i][j],j,P,route,lst)
    
    

if __name__ == '__main__':
    #matrix = [[1,2,1],[1,3,1],[3,4,1]]
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    #start = 1;end = 4; total = 4
    start = 2;end = 4;total =4
    print(homework_5(matrix, start, end, total))
    