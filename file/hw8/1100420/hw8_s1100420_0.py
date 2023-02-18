def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    if N == 0:
        return []
    a=queen(N,state=())
    b=trans(a)
    return b

#皇后的攻擊範圍
def attack(state, X):
    Y = len(state)
    return any(abs(state[i] - X ) in (0, Y-i)for i in range(Y))

#算出皇后位置
def queen(N, state=()):
    if len(state) == N:
        return [()]
    ans = []
    for pos in range(N):
        if not attack(state, pos):
            ans+=[(pos,)+ result for result in queen(N, state+(pos,))]
    return ans

#將皇后的位置設成Q，其餘設成-
def trans(state):
    if len(state) == 0:
        return []
    c = len(state[0])   
    d = len(state)
    _set =[ ]
    for i in range(d):
        board = ["-"*c]*c    #先填滿-在矩陣裡
        for j in range(c):
            loc = state[i][j]    #皇后所在的位子
            board[j] = board[j][:loc] +"Q"+ board[j][loc+1:]    #把皇后的位子換上Q
        _set.append(board)
    return _set

    return 

if __name__ == '__main__':
    N = 5
    print(homework_8(N))
    # [["Q"]]
    