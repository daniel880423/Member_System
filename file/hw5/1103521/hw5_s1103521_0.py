def homework_5(matrix, start, end, total):  # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    n = len(matrix) + 1
    path = [[-1 for _ in range(n)] for _ in range(n)]  # path

    A = [[None for _ in range(n)] for _ in range(n)]  # graph

    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = 0
            else:
                A[i][j] = float("inf")
    for a, b, c in matrix:
        A[a - 1][b - 1] = c

    for k in range(total):  # Floyd code
        for i in range(n):
            for j in range(n):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
                    path[i][j] = k
    global m
    m = ""
    def getpath(i, j):
        global m
        if path[i][j] != -1:
            getpath(i, path[i][j])
            m += str(path[i][j] + 1)
            getpath(path[i][j], j)

    getpath(start-1,end-1)
    answer_b = str(start) + m + str(end)
    answer = [A[start - 1][end-1],answer_b]
    if A[start - 1][end-1] == float("inf") or start == end:
        return [-1,None]
    return answer


if __name__ == '__main__':
    matrix = [[1, 2, 1], [1, 3, 3], [2, 1, 2],[3, 4, 4]]
    start = 2
    end = 4
    total = 4
    print(homework_5(matrix, start, end, total))
