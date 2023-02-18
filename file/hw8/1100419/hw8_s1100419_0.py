def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if N==0 :
        return []
    a=queens(N, state=())
    b=trans(a)
    return b

def conflict(state, nextX):    
    nextY = len(state)
    if any(abs(state[i] - nextX)== 0 for i in range(len(state))): #同行
        return True
    if any(abs(state[i] - nextX)== nextY - i for i in range(len(state))): #同對角線
        return True
    return False
    
def queens(N, state=()):
    z=len(state)
    if z==N:
        return [()]
    ans = []
    for pos in range(N):
        if not conflict(state, pos):
            ans += [(pos,)+ result for result in queens(N, state + (pos,))]
    return ans

def trans(state):
    c = len(state[0])   
    d = len(state)
    if d==0:
        return []
    _all =[ ]
    for i in range(d):
        board = ["-"*c]*c    #先填滿-在矩陣裡
        for j in range(c):
            loc = state[i][j]    #皇后所在的位子
            board[j] = board[j][:loc] +"Q"+ board[j][loc+1:]    #把皇后的位子換上Q
        _all.append(board)
    return _all



if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    