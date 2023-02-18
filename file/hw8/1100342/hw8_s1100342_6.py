def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    if N== 0:
        return []
    col=set()#行
    l_slash=set()#左斜線
    r_slash= set()#右斜線
    ans= []
    # global count
    # count =0
    #初始化輸出list
    Queens =[["-"]*N for i in range(N)]
    def backtrack(r):
        # global count
        # r=N時，表示找到一個解
        if r ==N:
            queen= ["".join(row)for row in Queens]
            ans.append(queen)
            # count+=1
            return
        for c in range(N):
            #同列、同對角線會被攻擊，直接跳過
            if c in col or (r+c)in l_slash or (r-c)in r_slash:
                continue
            ##找到一個Q並紀錄此Q會攻擊的位置
            col.add(c)
            l_slash.add(r+c)
            r_slash.add(r-c)
            ##顯示找到的Q
            Queens[r][c]="Q"
            ##往下一行繼續尋找
            backtrack(r +1)
            ##若此行找不到一個解，刪除上一個Q及會攻擊的位置
            col.remove(c)
            l_slash.remove(r+c)
            r_slash.remove(r -c)
            ##恢復上一個狀態
            Queens[r][c]="-"
    ##從第0行開始檢查
    backtrack(0)
    return ans

if __name__ == '__main__':
    N =8
    print(homework_8(N))
    #[["Q"]]

