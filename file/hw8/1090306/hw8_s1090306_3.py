def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if N==0: return [] #如果N=0則回傳[]
    board = [['-'] * N for _ in range(N)]
    res = []
    def isVaild(board,row, col):
            #判斷同一列是否衝突
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False
            #判斷左上角是否衝突
        i = row -1
        j = col -1
        while i>=0 and j>=0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
            #判斷右上角是否衝突
        i = row - 1
        j = col + 1
        while i>=0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtracking(board, row, N):
            #如果走到最後一行，說明已經找到一個解
        if row == N:
            temp_res = []
            for temp in board:
                temp_str = "".join(temp)
                temp_res.append(temp_str)
            res.append(temp_res)
        for col in range(N):
            if not isVaild(board, row, col):
                continue
            board[row][col] = 'Q'
            backtracking(board, row+1, N)
            board[row][col] = '-'
    backtracking(board, 0, N)
    return res

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    