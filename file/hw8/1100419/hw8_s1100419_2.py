def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if N==0 :
        return []
    a=queens(N, state=())
    b=trans(a)
    return b
    #主程式

def conflict(state, nextX):    
    nextY = len(state)
    if any(abs(state[i] - nextX)== 0 for i in range(len(state))): #皇后的攻擊位置(同行)
        return True
    if any(abs(state[i] - nextX)== nextY - i for i in range(len(state))): #皇后的攻擊位置(同對角線)
        return True
    return False
    #確認位子是否會被攻擊

def queens(N, state=()):
    z=len(state)
    if z==N:
        return [()]
    ans = []
    for pos in range(N):
        if not conflict(state, pos):
            ans += [(pos,)+ result for result in queens(N, state + (pos,))]
    return ans
    #用迴圈找出皇后可以擺放的位置，並且確定不在攻擊的位子上

def trans(state): 
    d = len(state)
    if d==0:
        return [] #沒有東西時回傳[]
    c = len(state[0])
    board_all =[ ]
    for i in range(d):
        board = ["-"*c]*c    #先填滿-在矩陣裡
        for j in range(c):
            loc = state[i][j]    #皇后所在的位子
            board[j] = board[j][:loc] +"Q"+ board[j][loc+1:]    #把皇后的位子換上Q
        board_all.append(board)
    return board_all #回傳棋盤



if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    