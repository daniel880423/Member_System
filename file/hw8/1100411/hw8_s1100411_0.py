def homework_8(N): 
    def safe(r, c): #判斷是否在安全位置上
        n = len(state)
        for i in range(n):
            if state[i][c] == 'Q': #判斷是否以有棋子
                return False
            elif r-i >= 0:
                if c-i >= 0 and state[r-i][c-i] == 'Q':
                    return False
                elif c+i < n and state[r-i][c+i] == 'Q':
                    return False
            
        return True

    def solve(r):
        n = len(state)
        if r == n: #檢驗到最後一列
            ans.append(["".join(i) for i in state]) #把state中存放的答案回傳
            return ans
        for c in range(0,n):
            if safe(r,c):
                state[r][c] = 'Q'
                solve(r+1) #下一列
                state[r][c] = '-'
         
    state = [['-']*N for i in range(N)] #建立空棋盤
    ans =[]
    solve(0) #從零開始走訪
    return ans





    

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    