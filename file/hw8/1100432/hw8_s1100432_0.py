def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking

    matrix= (qs(N,()))
    paper = []
    for i in matrix:
        a = []
        for j in i:
            queens=""
            for k in range(N):
                if j !=k:
                    queens += "-"
                else:
                    queens += "Q"
            a.append(queens)
        paper.append(a)
    return paper
def dazz(level,x2):
    y2 = len(level)
    return any(abs(level[i]-x2) in (0,y2-i) for i in range(y2))
def qs (n,level):
    if len(level) == n:
        return[()]
    a = []
    for pal in range(n):
        if not dazz(level,pal):
            a += [(pal,)+ output for output in qs(n,level+(pal,))]
    return a
if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]