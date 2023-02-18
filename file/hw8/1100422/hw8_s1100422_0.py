def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    if N==0 :
        return []
    a = queen(N, state=())
    b = trans(a)
    return b

#皇后的攻擊範圍
def attack(state, X):    
    Y = len(state)
    return any(abs(state[i] - X) in (0, Y - i) for i in range(Y)) 

#計算出各列皇后的位置(數字)
def queen(N, state=()):
    if len(state) == N:
        return [()]    
    ans = []
    for pos in range(N):
        if not attack(state, pos):
            ans += [(pos,)+ result for result in queen(N, state + (pos,))]
    return ans

#把Q放在上方計算出的位置，其他換成-
def trans(state):
    if len(state)==0:
        return []
    c = len(state[0])   
    d = len(state)
    _all =[ ]
    for i in range(d):
        board = ["-"*c]*c    #把-先填入
        for j in range(c):
            loc = state[i][j]    #皇后的位子
            board[j] = board[j][:loc] +"Q"+ board[j][loc+1:]    #Q取代皇后
        _all.append(board)
    return _all



if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    
    