def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    
    def NQueens(n) :       
        
        if n == 0:
            return []
        ans = []
        backtrack(0,[],[],[],ans)     
        return ans 
    
    def backtrack(row, qList,lslash,rslash, ans):    #分別用qList,lslash,rslash記錄目前皇后的行、左、右斜線能走的路徑
        
        if row == N:                                 #當列數等於N             
            ans.append(["-"*x + "Q" + "-"*(N-1-x) for x in qList])      #印出此組解
            return 
        
        for col in range(N):                         #當列數小於N
            if col not in qList and row+col not in lslash and row-col not in rslash :   #如果這格其他皇后無法到達
                backtrack(row+1, qList+[col],lslash+[row+col],rslash+[row-col], ans)    #加入此格的行、左右斜線並往下一列搜尋 
                           
    return NQueens(N)
    
if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    