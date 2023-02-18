def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking

    anss = (queen(N,()))
    borad = [[]]
    storeans = []
    for i in anss:
        ans = []
        for j in i:
            queens=""
            for k in range(N):
                if j !=k:
                    queens += "-"
                else:
                    queens += "Q"
            ans.append(queens)
        storeans.append(ans)

    

            







    return storeans
def conflict(state,nextX):
    nextY = len(state)
    return any(abs(state[i]-nextX) in (0,nextY-i) for i in range(nextY))
def queen (n,state):
    if len(state) == n:
        return[()]
    ans = []
    for pos in range(n):
        if not conflict(state,pos):
            ans += [(pos,)+ result for result in queen(n,state+(pos,))]
    return ans
if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    