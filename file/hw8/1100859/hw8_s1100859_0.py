def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    def ABS(queens, xy_sub, xy_sum): #設置遞迴函式，三個參數分別為皇后位置，檢查xy座標有無皇后的參數
        put = len(queens) 
        if put == N: #假如放置皇后數量等於N，將答案加至list
            ans.append(queens) 
            return None 
        for queen in range(N): #在N*N的棋盤中，遞迴尋找可以放N個皇后的佈局
            if queen not in queens and put-queen not in xy_sub and put+queen not in xy_sum: 
                ABS(queens+[queen], xy_sub+[put-queen], xy_sum+[put+queen]) 


    ans = []
    ABS([],[],[])
    if N == 0:
        return []
    return [["-"*i + "Q" + "-"*(N-i-1) for i in sol] for sol in ans]















 