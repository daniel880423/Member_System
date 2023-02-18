def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking

    def conflict(state, nextX):    #確認皇后是否攻擊不到對方
        nextY = len(state)
        return any(abs(state[i] - nextX) in (0, nextY - i) for i in range(nextY))

    def queens(n, state=[]): #排列位置,state是位置紀錄
        if len(state) == n: #結束遞迴
            return [[]]
        ans = []
        for pos in range(n):  #一個個位置確認
            if not conflict(state, pos): #確認皇后是否攻擊不到對方
                ans += [[pos,]+ result for result in queens(n, state + [pos,])] #遞迴
        return ans

    def visualize(state):   #將queen中得到的ans轉換成Q得排列
        vis=['-'*len(state)] * len(state)
        for i ,item in enumerate(state):
            vis[i]=vis[i][:item]+"Q"+vis[i][item+1:]
        return vis
    ans=[]
    b=queens(N) #執行queen
    if N==0:
        return ans
    for i in range(len(b)):
        ans.append(visualize(b[i])) 

    return ans
if __name__ == '__main__':
    N = 0
    print(homework_8(N))
    # [["Q"]]
    