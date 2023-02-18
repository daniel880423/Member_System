 # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
def homework_8(N):
    def is_valid(board, row, col):
        # 檢查這一列是否有皇后
        for i in range(N):
            if board[i][col] == "Q":
                return False

        # 檢查左上方是否有皇后
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # 檢查右上方是否有皇后
        i, j = row, col
        while i >= 0 and j < N:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def dfs(board, row):
        if row == N and N!=0:
            # 找到一個合法解，將棋盤加入結果中
            result.append(["".join(row) for row in board])
            return

        for col in range(N):
            # 如果這一行的這一列可以放皇后
            if is_valid(board, row, col):
                # 將皇后放入棋盤中
                board[row][col] = "Q"
                # 繼續往下做搜尋
                dfs(board, row + 1)
                # 回溯，將皇后從棋盤中移除
                board[row][col] = "-"

    result = []
    board = [["-" for _ in range(N)] for _ in range(N)]
    dfs(board, 0)
    return result

print(homework_8(0))