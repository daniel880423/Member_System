def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    global col,rightSlash,leftSlash,ans,board
    if N<0 or N>9:#檢查N是否在範圍內
        return 0
    col=set()
    rightSlash=set()#r+c
    leftSlash=set()#r-c
    ans=[]
    board=[['-']*N for i in range(N)]
    backtracking(0,N)
    if ans==[[]]:
        ans=[]
    return ans
def backtracking(r,N):
    global col,rightSlash,leftSlash,ans,board
    if   r==N:
        sol=["".join(row) for row in board]
        ans.append(sol)
    for c in range(N):
        if c in col or r+c in rightSlash or r-c in leftSlash:
            continue
        col.add(c)
        rightSlash.add(r+c)
        leftSlash.add(r-c)
        board[r][c]="Q"

        backtracking(r+1, N)

        col.remove(c)
        rightSlash.remove(r+c)
        leftSlash.remove(r-c)
        board[r][c]="-"

        


if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    