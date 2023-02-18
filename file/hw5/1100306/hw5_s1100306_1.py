def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    # import sys
    # print(sys.setrecursionlimit(1000))
    global path
    
    
    #創建path
    path = [[0 for _ in range(total)] for _ in range(total)]
    for i in range(total):
        for j in range(total):
            path[i][j] = -1


    #創建A矩陣
    A = [[0 for _ in range(total)] for _ in range(total)]
    for i in range(total):
        for j in range(total):
            A[i][j] = float("inf")
            
            

    #將matrix輸入進A矩陣
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                A[i][j] = 0
            else:
                A[matrix[i][0]-1][matrix[i][1]-1] = matrix[i][2]

    #添加中轉點k至path
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
                    path[i][j] = k 
    
    answer = [0] * 2
    answer[0] = A[start - 1][end - 1]


    optpath = []
    middle_point = getpath(start - 1, end - 1, optpath)
    b = "".join([str(_) for _ in middle_point])
    answer[1] = str(start)  + str(b) + str(end)
    
    if path[start - 1][end - 1] == -1:
        answer[0] = -1
        answer[1] = None
    
    
    return answer

def getpath(i, j, optpath):    
    middle_point = str(path[i][j])
    
    if(path[i][j] != -1):
        getpath(i, path[i][j], optpath)
        middle_point = str(path[i][j]+1)
        optpath.append(middle_point)
        getpath(path[i][j], j, optpath)

    return optpath




if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    