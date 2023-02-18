def homework_8(N):
    each_ans_queen = []		                                            #存每一個解
    def find_queen_position(row, queen, N):                             #搜尋能放置皇后的位置       
        for column in range(N):                                         #換行
            available=True
            for i in range(row):                                            
                if queen[i] == column or abs(i-row) == abs(queen[i]-column):#有皇后與此位置同一行或在此位置的左右斜線上
                    available=False
                # if available(queen, row, column):        
            if available==True:                   
                queen[row] = column                                     #queen存當下解的皇后位置
                if row == N-1:                                          #最後一列已放置皇后
                    each_ans_queen.append(tuple(queen))                 
                    
                else:                                                   #還沒找到最後一列
                    find_queen_position(row+1, queen, N)
    # def available(queen, row, column):                                  # 判斷當下位置是否可放皇后
    #     # for i in range(row):                                            
    #     #     if queen[i] == column or abs(i-row) == abs(queen[i]-column):#有皇后與此位置同一行或在此位置的左右斜線上
    #             return False
    #     return True
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


# def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
#     # depth first search + backtracking
#     chessboard = [["-"]*N for x in range(N)]                        #預設一個空棋盤
#     j=0                                                             #從[0,0]開始
#     i=0
#     Ans=[]                                                          
#     global Q_num                                                    #全域變數Q_num存每次解填入的皇冠數
#     for j in range(N):                                              
#         row=[]                                                      #設row存不能走的列
#         column=[]                                                   #設column存不能走的行
#         right_slash=[]                                              #設right_slash存不能走的右斜線
#         left_slash=[]                                               #設left_slash存不能走的左斜線
#         Q_num=0
#         New_Ans=[]                                                  #每次找出的新解
#         DFS (i,j,row,column,right_slash,left_slash,chessboard,N)    #深度搜尋
#         if Q_num==N:                                                #皇冠數量正確
#             for row in range(N):
#                 chess="".join(chessboard[row])                      
#                 New_Ans.append(chess)                               
#             Ans.append(New_Ans)                                     #每次的新解加入Ans
#             chessboard = [["-"]*N for x in range(N)]                #重置為空棋盤找下個解
#         else:
#             chessboard = [["-"]*N for x in range(N)]
   
#     return Ans

# def DFS (i,j,row,column,right_slash,left_slash,chessboard,N):
#     global Q_num
#     if (i-j not in right_slash) and (i+j not in left_slash) and (i not in row) and (j not in column):#如果位置[i,j]符合能放皇冠條件
#         chessboard[i][j]="Q"                                                                         #放置皇冠
#         Q_num+=1
#         row.append(i)                                                                                #加入因位置[i,j]而不能走的路徑
#         column.append(j)                                                                             
#         right_slash.append(i-j)
#         left_slash.append(i+j)
#     if j<N-1 and i<=N-1:
#         DFS (i,j+1,row,column,right_slash,left_slash,chessboard,N)
#     elif j==N-1 and i<N-1:
#         DFS (i+1,0,row,column,right_slash,left_slash,chessboard,N)
