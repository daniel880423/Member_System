def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if N==0:
        return []
    def conflict(state, nextX):
        nextY = len(state)
        return any(abs(state[i] - nextX) in (0, nextY - i) for i in range(nextY))
    def queens(n, state=()):
        if len(state) == n:
            return [()]
        ans = []
        for pos in range(n):
            if not conflict(state, pos):
                ans += [(pos,)+ result for result in queens(n, state + (pos,))]
        return ans
    def plot_queen(queen, n):
        out = []
        for i in range(n):
            s = '-' * queen[i] + 'Q' * 1 + '-' * (n-queen[i]-1)
            out.append(s)
        return out
    queen = [-1 for _ in range(N)]
    out = []
    for t in queens(N):
        out.append(plot_queen(t, N))
    return out
     
    









if __name__ == '__main__':
    N = 0
    print(homework_8(N))
    # [["Q"]]
    