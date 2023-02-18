def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    #如果N=0代表需要排的皇后為零個，因此回傳空list。
    if N==0:
        ans = []
        return ans

    #此函式為回溯，參數為矩陣board和列row。
    def backtrack(board, row):
        #當現在走訪到的列數大於或等於N時代表N個皇后已排列完成，cur_ans代表暫存答案字串，把cur_ans存進ans裡。
        if row >= N:
            cur_ans = [''.join(row) for row in board]
            ans.append(cur_ans)

        #for迴圈代表行數從0跑到N-1，進入迴圈後需判斷目前皇后的位置是否可擺放，呼叫queen函式。
        #若可擺放把目前位置的字元設為'Q'，代表有QUEEN在這個位置上。
        #接著呼叫backtrack做遞迴，列數改為下一列。
        #若下一列有可擺放的位置，但擺放後會造成下一列無法擺放其他皇后，此時須把目前位置的字元設為'-'。
        for l in range(N):
            if queen(row, l):
                board[row][l] = 'Q'
                backtrack(board, row+1)
                board[row][l] = '-'

    #此函式為判斷目前的子樹是否為promising
    def queen(row, col):
        #此for巢狀迴圈在寫判斷目前這列之上方的每一列，若有皇后存在，需檢查是否為同行或同右斜線或同左斜線。
        #若上述條件符合，則回傳False，代表不能擺放新皇后；反之，若上述條件不符合，則回傳True，代表可以擺放新皇后。
        for i in range(row):
            for j in range(N):
                if board[i][j] =='Q':
                    if j == col or i+j == row+col or i-j == row-col:
                        return False
        return True

    #初始化區
    ans=[] #ans用來存放最後的答案字串
    board = [['-']*N for k in range(N)] #board代表的是N*N的棋盤格，每個元素皆為-。
    backtrack(board, 0) #呼叫backtrack，從第0列開始。

    #回傳最終所有可能結果
    return ans 


if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    