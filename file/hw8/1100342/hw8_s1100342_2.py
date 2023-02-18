def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    if N ==0:
        return []

    def queens(n, placed=()):
        #當長度為N時，表示找到一個解，並記錄下來
        if len(placed) == n: 
            return [()]
        ans = []
        for x in range(n):
            #若不會被攻擊
            if not nonpromsing(placed, x):
                #ans加入所有可能的解
                ans += [(x,)+ result for result in queens(n, placed + (x,))]
        return ans

    ans = []
    #印出所有可能解
    for i in queens(N):
        ans.append(print_ans(i))
    return ans
def nonpromsing(placed, k):
#placed 為已放置Q，下一個Q放在第k行
    col = len(placed)
    #在同行或同對角線會被攻擊
    attacked = any(abs(placed[i] - k) in (0, col - i) for i in range(col))
    return attacked
def print_ans(placed):
    #初始化p陣列為N*N
    p=['-'*len(placed)] * len(placed)
    for i ,Q in enumerate(placed):
        #第Q項顯示Q，其他維持-
        p[i]=p[i][:Q]+"Q"+p[i][Q+1:]
    return p    

    

if __name__ == '__main__':
    N =4
    print(homework_8(N))
    # [["Q"]]
    