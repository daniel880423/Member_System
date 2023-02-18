def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    as= (Q(N,()))
    white = []
    for i in as:
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
def B(level,X1):
    Y1 = len(level)
    return any(abs(level[i]-X1) in (0,Y1-i) for i in range(Y1))
def C (n,LV):
    if len(LV) == n:
        return[()]
    a = []
    for rel in range(n):
        if not B(LV,rel):
            a += [(rel,)+ END for END in C(n,LV+(rel,))]
    return a
    
if __name__ == '__main__':
    N = 4
    print(homework_8(N))