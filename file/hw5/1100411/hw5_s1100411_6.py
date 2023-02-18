def homework_5(matrix, start, end, total): 
    A = [[float("inf") for j in range(total)]for k in range(total)]
    getpath = [[ -1 for j in range(total)]for k in range(total)]
    #整理出路徑
    for i in range(total):
        A[i][i] = 0
    for i in range(len(matrix)):
        A[matrix[i][0]-1][matrix[i][1]-1] = matrix[i][2]
    #最短路徑
    for i in range(total):
        for j in range(total):
            for k in range(total):
                if A[i][k] + A[k][j] < A[i][j]:
                    if getpath[i][k] != -1 and getpath[k][j] != -1:
                        getpath[i][j] = getpath[i][k]+str(k+1)+getpath[k][j]
                    elif getpath[i][k] != -1 :
                        getpath[i][j] = getpath[i][k]
                        getpath[i][j] += str(k+1)
                    elif getpath[k][j] != -1:
                        getpath[i][j] = str(k+1)
                        getpath[i][j] += str(getpath[k][j])
                    
                    else:
                        getpath[i][j] = str(k+1)
                    A[i][j] = A[i][k] + A[k][j]
                    
    
    #答案
    
    ans = []
    if A[start-1][end-1] == float("inf") or A[start-1][end-1] == 0:
        ans = [-1, None]
    else:
        ans.append(A[start-1][end-1])
        if getpath[start-1][end-1] == -1:
            ans.append(str(start)+str(end))
        else:
            ans.append(str(start)+str(getpath[start-1][end-1])+str(end))

    return ans
if __name__ == '__main__':
    matrix = [[2, 5, 6], [2, 3, 2], [2, 4, 1], [3, 5, 3], [4, 5, 16], [4, 2, 2], [7, 8, 5], [8, 6, 6], [3, 6, 1], [4, 7, 1], [6, 4, 3], [7, 3, 3], [8, 7, 10]]
    start = 8;end = 5; total = 8
    print(homework_5(matrix, start, end, total))
    