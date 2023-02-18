def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    N = int(input())
    global ans
    ans=[]
    board=[['–' for x in range(N)] for y in range(N)]
    def isSafe(board, r, c): #檢查兩皇后有沒有互相攻擊
        #兩皇后在同行回傳False
        for i in range(r):         
            if board[i][c] == 'Q':
                return False
        
        #兩皇后在同\對角線回傳False
        i=r
        j=c
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i=i-1
            j=j-1
        #兩皇后在同\對角線回傳False
        i=r
        j=c
        while i>=0 and j<len(board):
            if board[i][j] == 'Q':
                return False
            i=i-1
            j=j+1
        return True
    def printans(board):
        b=[]
        global c
        c=''
        for i in board:
            c+=''.join(i)+','
            c=c[:-1]
            b.append(c)
            c=''
        ans.append(b)
    def nQueen(board, r):
        #放n個皇后就回傳答案
        if r == len(board):
            printans(board)
            return
        for i in range(len(board)):
            if isSafe(board, r, i):
                #安全就放皇后
                board[r][i] = 'Q'
                #下一列
                nQueen(board, r + 1)
                #回溯
                board[r][i] = '–'
    nQueen(board, 0)
    return ans

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    