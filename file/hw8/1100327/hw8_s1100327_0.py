def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    global col,rightSlash,leftSlash,ans,board
    if N<0 or N>9:#檢查N是否在範圍內
        return 0
    col=set()
    rightSlash=set()#r+c
    leftSlash=set()#r-c
    ans=[]
    board=[['-']*N for i in range(N)]#創建棋盤格
    backtracking(0,N)
    if ans==[[]]:
        ans=[]
    return ans
def backtracking(r,N):
    global col,rightSlash,leftSlash,ans,board
    if   r==N:
        sol=["".join(row) for row in board]#把每行的解放進ans內
        ans.append(sol)
    for c in range(N):
        if c in col or r+c in rightSlash or r-c in leftSlash:#判斷這個格子能不能放皇后，不能就跳過
            continue
        col.add(c)##########
        rightSlash.add(r+c)#新找到能放皇后的參數加入col,slash
        leftSlash.add(r-c)##
        board[r][c]="Q"#

        backtracking(r+1, N)#遞迴下一個格子

        col.remove(c)##########
        rightSlash.remove(r+c)#不能放皇后的把參數移出來
        leftSlash.remove(r-c)##
        board[r][c]="-"

        


if __name__ == '__main__':
    N = 8

    print(homework_8(N))
    # [["Q"]]
    