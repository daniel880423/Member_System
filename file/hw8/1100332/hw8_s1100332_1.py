
# depth first search + backtracking
def homework_8(N):
    result = []
    board = [['-' for _ in range(N)] for _ in range(N)]
    def homework_8(board, row):
        if row == N:
            result.append(board)
            return True

        for col in range(N):
            if not is_valid(board, row, col):
                continue

            board[row][col] = 'Q'
            if homework_8(board, row + 1):
                return True
            board[row][col] = '-'

        return False

    def is_valid(board, row, col):
        for i in range(N):
            if board[i][col] == 'Q':
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True



    homework_8(board, 0)
    return result