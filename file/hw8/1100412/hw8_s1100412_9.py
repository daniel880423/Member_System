def homework_8(N):
    if N==0:                                                                            #0x0無法放置皇后
        return []
    each_ans_queen = []		                                                            #存每一個解
    def find_queen_position(row, N, col, rs, ls):                                       #搜尋能放置皇后的位置    
        if row == N:                                                                    #最後一列已放置皇后
            each_ans_queen.append(tuple(col))                                           #講本次解存入each_ans_queen
            return
        for column in range(N):                                          
            if column not in col and (row-column) not in rs and (row+column) not in ls: #有皇后與此位置同一行或在此位置的左右斜線上

                col.append(column)                                                      #存不能放皇后的位置         
                rs.append(row-column)
                ls.append(row+column)
                find_queen_position(row+1, N, col,rs,ls)                                #還沒找到最後一列
                col.pop()
                rs.pop()
                ls.pop()
    def plot_queen(each_ans_queen, N):
        chessboard = []                                                                 #預設棋盤
        for i in range(N):                       
            row_i = '-' * each_ans_queen[i] + 'Q' + '-' * (N-each_ans_queen[i]-1)       #放置皇后
            chessboard.append(row_i)
        return chessboard

    find_queen_position(0,N, [], [], [])
    Ans = []
    for each_ans in each_ans_queen:                                                     #將每個解轉換成棋盤形式輸出           
        Ans.append(plot_queen(each_ans, N))
    return Ans    





if __name__ == '__main__':
    N = 4
    print(homework_8(N))
