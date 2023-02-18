def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if N==0:
        ans=[]
        return ans

    #def isValid(row, col):
        # 如果該點所對應的右斜線或左斜線或列已經放置皇后則回傳False
        #if (col in col_hash) or ((row + col) in pie_hash) or ((row-col) in na_hash):
            #return False
        #return True

    def backtrack(board, row):
        if row >= N:
            cur_ans = [''.join(row) for row in board]
            ans.append(cur_ans)

        for col in range(N):
            if (col not in col_hash) and ((row + col) not in pie_hash) and ((row-col) not in na_hash):
                board[row][col] = 'Q'
                pie_hash.add(row + col)
                na_hash.add(row - col)
                col_hash.add(col)

                backtrack(board, row+1)

                board[row][col] = '-'
                pie_hash.remove(row + col)
                na_hash.remove(row-col)
                col_hash.remove(col)


    ans = []
    board = [['-'] * N for _ in range(N)]
    pie_hash = set() # 紀錄已放置皇后的右斜線
    na_hash = set()  # 紀錄已放置皇后的左斜線
    col_hash = set() # 紀錄已放置皇后的列
    backtrack(board,0)

    #回傳最終所有可能結果
    return ans

    
if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    