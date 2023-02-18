def homework_5(matrix, start, end, total):
    # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    if start == end:
        return[-1, None]
    a = [[float("inf")]*total for _ in range(total)]
    p = [[-1]*total for _ in range(total)]
    l = len(matrix)
    for n in range(l):
        i = matrix[n][0]
        j = matrix[n][1]
        k = matrix[n][2]
        a[i-1][j-1] = k
    for i in range(total):
        a[i-1][i-1] = 0
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if (a[i-1][k-1] + a[k-1][j-1] < a[i-1][j-1]):
                    a[i-1][j-1] = min(a[i-1][j-1], a[i-1][k-1]+a[k-1][j-1])
                    p[i-1][j-1] = k
                    
    if a[start-1][end-1] == float('inf'):
        return[-1, None]
    path = str(start)
    for j in range(end):
        if p[start-1][j]!=-1:
            path += str(p[start-1][j]) 
    path += str(end)
    return[a[start-1][end-1], path]
    
if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2
    end = 3
    total = 4
    print(homework_5(matrix, start, end, total))