 # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
def homework_8(N: int):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i][col] == "Q":
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = row - 1, col + 1
        while i >= 0 and j < N:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def dfs(board, row):
        if row == N:
            result.append(board.copy())
            return

        for col in range(N):
            if is_valid(board, row, col):
                board[row][col] = "Q"
                dfs(board, row + 1)
                board[row][col] = "-"

    result = []
    dfs([["-" for _ in range(N)] for _ in range(N)], 0)
    return result