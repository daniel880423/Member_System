def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    chessboard = [["-"]*N for x in range(N)]                        #預設一個空棋盤
    Ans=[]                                                          
    global Q_num                                                    #全域變數Q_num存每次解填入的皇冠數
    for j in range(N):        
        i=0                                                             #從第0列第0行開始                                     
        row=[]                                                      #設row存不能走的列
        column=[]                                                   #設column存不能走的行
        right_slash=[]                                              #設right_slash存不能走的右斜線
        left_slash=[]                                               #設left_slash存不能走的左斜線
        Q_num=0
        New_Ans=[]                                                  #每次找出的新解
        DFS (i,j,row,column,right_slash,left_slash,chessboard,N)    #深度搜尋
        if Q_num==N:                                                #皇冠數量正確
            for row in range(N):
                chess="".join(chessboard[row])                      
                New_Ans.append(chess)                               
            Ans.append(New_Ans)                                     #每次的新解加入Ans
            chessboard = [["-"]*N for x in range(N)]                #重置為空棋盤找下個解
        else:
            chessboard = [["-"]*N for x in range(N)]
   
    return Ans

def DFS (i,j,row,column,right_slash,left_slash,chessboard,N):
    global Q_num
    if (i-j not in right_slash) and (i+j not in left_slash) and (i not in row) and (j not in column):#如果位置[i,j]符合能放皇冠條件
        chessboard[i][j]="Q"                                                                         #放置皇冠
        Q_num+=1
        row.append(i)                                                                                
        column.append(j)                                                                             
        right_slash.append(i-j)
        left_slash.append(i+j)
    if j<N-1 and i<=N-1:                                                                             #若還沒找完一整列 
        DFS (i,j+1,row,column,right_slash,left_slash,chessboard,N)                                   #換行
    elif j==N-1 and i<N-1:                                                                           #若已找完一整列
        DFS (i+1,0,row,column,right_slash,left_slash,chessboard,N)                                   #換列從頭找起





if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
