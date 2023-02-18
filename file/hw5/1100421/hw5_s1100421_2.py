def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path = [[-1]*total for _ in range(total)]
    A = [[0]*total for _ in range(total) ]
    for i in range(len(matrix)):
        if i>=len(matrix):
                break
        for j in range(total):
            tmp_i = matrix[i][j]
            tmp_j = matrix[i][j+1]
            A[tmp_i-1][tmp_j-1] = matrix[i][j+2]
            break
    for i in range(total):
        for j in range(total):
            if i != j and A[i][j] == 0:
                A[i][j] = float("inf")
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = min(A[i][k] + A[k][j], A[i][j])
                    path[i][j] = k+1
    lst = [start]
    getpath(start, end, path, lst)
    lst.append(end)
    ans_lst = ""
    for x in lst:
        ans_lst += str(x)
    step = A[start-1][end-1]
    if step == float("inf"):
        step = -1
        ans_lst = None
    ans_lst = [step, ans_lst]
    return ans_lst

def getpath(start, end, path, lst):
    if path[start-1][end-1] != -1:
        getpath(start, path[start-1][end-1], path, lst)
        lst.append(path[start-1][end-1])
        getpath(path[start-1][end-1], end, path, lst)

if __name__ == '__main__':
    matrix =   [[1,2,5],[2,3,1],[2,5,4],[3,4,3],[4,6,5],[6,7,2],[2,6,8],[5,7,5],[6,8,2],[7,9,4],[8,9,1],[9,10,10],[9,11,2],[10,11,2],[11,12,2]]
    start = 2; end = 12; total = 12
    print(homework_5(matrix, start, end, total))
    