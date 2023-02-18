def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    high= (ans(N,()))
    slate = []
    for i in high:
        a = []
        for j in i:
            Q=""
            for k in range(N):
                if j !=k:
                    Q += "-"
                else:
                    Q += "Q"
            a.append(Q)
        slate.append(a)
    return slate
def moto(level,x2):
    y2 = len(level)
    return any(abs(level[i]-x2) in (0,y2-i) for i in range(y2))
def ans (n,level):
    if len(level) == n:
        return[()]
    a = []
    for pal in range(n):
        if not moto(level,pal):
            a += [(pal,)+ output for output in ans(n,level+(pal,))]
    return a
if __name__ == '__main__':
    N = 4 
    print(homework_8(N))
    # [["Q"]]
    