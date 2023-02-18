def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    #如果N等於0，則沒有皇后需要擺放。
    if N==0:
        ans=[]
        return ans

    #回溯函式
    def backtrack(board, row):
        #如果列的個數已超過N，則把答案存在ans裡。
        if row >= N:
            cur_ans = [''.join(row) for row in board]
            ans.append(cur_ans)
        #for迴圈代表行數，判斷現在位置是否有與其他已擺放之皇后重疊，包括同一行、右斜線、左斜線。
        #若沒有重疊則擺放新皇后，並將新皇后的列和斜線存進right_hash、left_hash、col_hash裡。
        #遞迴呼叫自己本身，列數改為下一列。
        #若有重疊則不擺放新皇后，並將現在位置的列和斜線從right_hash、left_hash、col_hash移除。
        for col in range(N):
            if (col not in col_hash) and ((row + col) not in right_hash) and ((row-col) not in left_hash):
                board[row][col] = 'Q'
                right_hash.add(row + col)
                left_hash.add(row - col)
                col_hash.add(col)
                backtrack(board, row+1)
                board[row][col] = '-'
                right_hash.remove(row + col)
                left_hash.remove(row-col)
                col_hash.remove(col)


    ans = [] #用來收集可能的擺放組合
    board = [['-'] * N for _ in range(N)] #N*N棋盤格
    right_hash = set() # 紀錄已放置皇后的右斜線
    left_hash = set()  # 紀錄已放置皇后的左斜線
    col_hash = set() # 紀錄已放置皇后的列
    backtrack(board,0) #呼叫回溯函式，從第0列開始。

    #回傳最終所有可能結果
    return ans

    
if __name__ == '__main__':
    N = 4
    # [["Q"]]
    