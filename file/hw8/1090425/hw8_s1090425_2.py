def homework_8(N):
    # depth first search + backtracking
    global queen                               #皇后位置
    global number                              #解的編號
    global ans                                 #回傳的答案陣列
    global size                                
    size = N                                   #大小為N*N棋盤
    ans = [[None]]       #宣告為二維空陣列以存放所有的解
    number=0                                   #初始化編號
    queen=[None]*size                          #存放n個皇后之列位置
    position(0)                                #從第零列第零行開始深度走訪
    i=0
    while i < len(ans):                        #刪除答案陣列中多餘項目
        if ans[i] == [None]:
            del ans[i]
            i-=1
        i+=1
            
    return ans

def position(col):                               
    global queen
    global size
    row = 0
    while row<size:                           
        if attack(row,col)!=1:           #沒被攻擊
            queen[col]=row               #紀錄皇后位置給後面的皇后做判斷
            if col==size-1:
                create_lst()
            else:                        #被攻擊的話
                position(col+1)          #找下一種解 
        row=row+1                        #被攻擊所以找下一個位置               

def attack(row, col):
    global queen
    i = 0
    atk = 0
    slash_row = slash_col = 0
    while (atk != 1) and i < col:
        slash_col = abs(i-col)
        slash_row = abs(queen[i]-row)   #判斷皇后是否在同一列在同一對角線上
        if queen[i] == row or slash_row == slash_col:
            atk = 1
        i = i+1
    return atk

def create_lst():
    global number
    global ans
    global size
    x=y=0
    ans.append(ans[number])
    ans[number]=[]
    s=""
    for x in range(size):
        for y in range(size):
            if y==queen[x]:
                s=s+"Q"
            else:
                s=s+"-"
        ans[number].append(s)
        s=""
    number+=1



    
if __name__ == '__main__':
    N=4
    print(homework_8(N))
    
