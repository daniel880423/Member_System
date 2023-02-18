def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    board = [['-'] * N for _ in range(N)]
    res = []
    if N == 0: #如果N=0則回傳[]
        return res

    def backtrack(row): #表示board中小於row的那些行（row上面的那些行）已經放置皇後了，這一步開始往第row行放皇後
        n = len(board)
        if row == N: #到最後一行將結果添加到res
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

def isValid(board, row, col): #查看是否可以在board[row][col]的位置放置皇後
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
    N = 0
    print(homework_8(N))
    # [["Q"]]
    