def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    if N<0 or N>9:#檢查N是否在範圍內
        return 0
    global ChessBoard
    global Queen_index
    ans=[]
    for i in range(N):
        ChessBoard=[['-' for i in range(N)]for i in range(N)]#創建棋盤
        Queen_index=[]
        ChessBoard[0][i]='Q'#放置第一個皇后
        Queen_index.append((0,i))#Queen_index用來記錄有放置皇后的座標
        DFS(1, 0, N)#從第二行開始進行遞迴
        if sort(ChessBoard)!=None:#把滿足放滿N個皇后的解放入ans
            ans.append(sort(ChessBoard))          
    return ans

def DFS(row,column,N):
    global ChessBoard
    global Queen_index
    if row<N and column<N:#遞迴的終止條件
        if valid(row,column):#如果經過判斷這格可以放皇后就
            Queen_index.append((row,column))#如果經過valid判斷這格可以放皇后就把座標放入Queen_index
            ChessBoard[row][column]='Q'#放置皇后
            DFS(row+1, 0, N)#尋找下一行是否有位置可以放皇后
        else: 
            if column==N-1:#若最後一列也不能放皇后了那就終止遞迴
                return 0
            else:
                DFS(row, column+1, N)    

def valid(row,column):
    global ChessBoard
    global Queen_index
    for i in Queen_index:
        if i[0]==row or i[1]==column or abs(row-i[0])==abs(column-i[1]):#若對角線、行、列上有其他皇后那就回傳false
            return False
    return True

def sort(ChessBoard):#把答案整理成List[str]並回傳
    sol=[]
    for i in ChessBoard:
        if 'Q' not in i:
            return None
        a=''
        for j in i:
            a+=j 
        sol.append(a)
    return sol   
       
        


if __name__ == '__main__':
    N = 3
    print(homework_8(N))
    # [["Q"]]
    