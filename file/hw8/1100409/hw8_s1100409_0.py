def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    box= (Q(N,()))
    white = []
    for i in box:
        a = []
        for j in i:
            QUEEN=""
            for k in range(N):
                if j !=k:
                    QUEEN += "-"
                else:
                    QUEEN += "Q"
            a.append(QUEEN)
        white.append(a)
    return white
def SOFT(level,X1):
    Y1 = len(level)
    return any(abs(level[i]-X1) in (0,Y1-i) for i in range(Y1))
def Q (n,LV):
    if len(LV) == n:
        return[()]
    a = []
    for SOL in range(n):
        if not SOFT(LV,SOL):
            a += [(SOL,)+ END for END in Q(n,LV+(SOL,))]
    return a
    
if __name__ == '__main__':
    N = 4
    print(homework_8(N))