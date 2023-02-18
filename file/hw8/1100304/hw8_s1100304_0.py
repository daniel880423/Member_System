def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    
    def trackback(board, row):  # 從(0, 0)開始放皇后
        if row == len(board):
            lst.append(["".join(i) for i in board])
            return
            
        for col in range(len(board)):
            if not isValid(board, row, col):
                continue
            board[row][col] = 'Q'
            trackback(board, row + 1)
            board[row][col] = '-'
   

    def isValid(board ,row, col): # 是否可以在board[row][col]放置皇后
        for i in range(len(board)): # 如果第col列上存在Q==>False
            if board[i][col] == 'Q':
                return False
        
        i,j = row-1, col+1          # 檢查右上方是否有皇后
        while i >=0 and j < len(board):   
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
       
        i,j = row-1, col-1          # 檢查左上方是否有皇后
        while i >= 0 and j >= 0:  
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        return True
    
    
    lst = []
    board = []
    for i in range(N):    #建立 N x N 棋盤
        board.append([])
        for j in range(N):
            board[i].append("-")
            
    trackback(board, 0)
    
    if N == 0:
        return []
    else:
        return lst
    
if __name__ == '__main__':
    N = 4
    print(homework_8(N))
