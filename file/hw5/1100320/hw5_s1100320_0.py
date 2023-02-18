from math import inf


def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    global node
    node =''
    A = [[float('inf') for i in range(total)] for j in range(total)]
    path = [[-1 for i in range(total)] for j in range(total)]
    
    for m in range(total):
        for n in range(total):  
            for k in matrix:
                if k[0] == m+1 and k[1] == n+1:
                    A[m][n] = k[2]

    for k in range(total):
        for i in range(total):
            for j in range(total):
                if (A[i][k] + A[k][j]) < A[i][j]:
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
                    path[i][j] = k
    ans_path = A[start-1][end-1]

    def getpath(l, p):
        global node
        if path[l][p] != -1:
            getpath(l, path[l][p])
            node += str((path[l][p])+1)
            getpath(path[l][p], p)
    getpath(start-1, end-1)

    ans_str = str(start)+ str(node) + str(end)
    if A[start-1][end-1] == float('inf'):
        ans_str = None
        ans_path = -1
    ans_lst = [ans_path, ans_str]
    return ans_lst



if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2;end = 3; total = 4
    print(homework_5(matrix, start, end, total))
    