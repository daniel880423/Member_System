def homework_8(N):
    if N==0:
        return []
    def conflict(state, nextX): #檢查同行/對角線是否有其他皇后
        nextY = len(state)
        return any(abs(state[i] - nextX) in (0, nextY - i) for i in range(nextY))
    def queens(n, state=()):
        if len(state) == n:
            return [()]
        ans = [] #記錄在state棋子已經放好的狀況下，後續的所有解答
        for pos in range(n): #嘗試在下一列中放新的皇后
            if not conflict(state, pos):
                ans += [(pos,)+ result for result in queens(n, state + (pos,))]
        return ans
    def plot_queen(queen, n): #把棋盤填上空格與Q
        out = []
        for i in range(n):
            s = '-' * queen[i] + 'Q' * 1 + '-' * (n-queen[i]-1)
            out.append(s)
        return out
    queen = [-1 for _ in range(N)] #空棋盤
    out = []
    for t in queens(N):
        out.append(plot_queen(t, N))
    return out
     
    









if __name__ == '__main__':
    N = 0
    print(homework_8(N))
    # [["Q"]]
    