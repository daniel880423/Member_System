def homework_8(N):
    each_ans_queen = []		                                            #存每一個解
    def find_queen_position(row, queen, N):                             #搜尋能放置皇后的位置       
        for column in range(N):                                         #換行
            if available(queen, row, column):                           
                queen[row] = column                                     #queen存當下解的皇后位置
                if row == N-1:                                          #最後一列已放置皇后
                    each_ans_queen.append(tuple(queen))                 
                    
                else:                                                   #還沒找到最後一列
                    find_queen_position(row+1, queen, N)
    def available(queen, row, column):                                  # 判斷當下位置是否可放皇后
        for i in range(row):                                            
            if queen[i] == column or abs(i-row) == abs(queen[i]-column):#有皇后與此位置同一行或在此位置的左右斜線上
                return False
        return True
    def plot_queen(each_ans_queen, N):
        chessboard = [["-"]*N for x in range(N)]                        #預設棋盤
        for i in range(N):
            chessboard[i][each_ans_queen[i]]='Q'                        #放置皇后
                
        for row in range(N):
            new="".join(chessboard[row])                      
            chessboard[row]=new
        return chessboard

    queen = ['queen_pos']*N                                             #存皇后位置
    find_queen_position(0, queen, N)
    Ans = []
    for each_ans in each_ans_queen:                                            
        Ans.append(plot_queen(each_ans, N))
    return Ans    





if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
