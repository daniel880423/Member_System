 # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
def homework_8(N):
    def is_valid(board, row, col):
        for i in range(N):
            if board[i][col] == "Q":
                return False

        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i >= 0 and j < N:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def dfs(board, row, cols, diagonals1, diagonals2):
        if row == N:
            result.append(["".join(row) for row in board])
            return

        for col in range(N):
            if cols[col] and diagonals1[row + col] and diagonals2[row - col]:
                board[row][col] = "Q"
                cols[col] = False
                diagonals1[row + col] = False
                diagonals2[row - col] = False
                dfs(board, row + 1, cols, diagonals1, diagonals2)
                board[row][col] = "-"
                cols[col] = True
                diagonals1[row + col] = True
                diagonals2[row - col] = True

    result = []
    board = [["-" for _ in range(N)] for _ in range(N)]
    cols = [True for _ in range(N)]
    diagonals1 = [True for _ in range(2 * N - 1)]
    diagonals2 = [True for _ in range(2 * N - 1)]
    dfs(board, 0, cols, diagonals1, diagonals2)
    return result