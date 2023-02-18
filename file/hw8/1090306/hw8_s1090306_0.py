def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    board = [['-'] * N for _ in range(N)]
    res = []
    def backtrack(row):
        n = len(board)
        if row == N:
            tmp = [''.join(i) for i in board]
            res.append(tmp)
            return

        for col in range(N):
            if not isValid(board, row, col):
                continue
            board[row][col] = 'Q'
            backtrack(row + 1)
            board[row][col] = '-'
    backtrack(0)

    return res 

def isValid(board, row, col):
    n = len(board)
    
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
        if board[i][j] == 'Q':
            return False
    
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    return True

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    