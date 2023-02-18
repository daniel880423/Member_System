def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    
    def NQueens(n) :       
        if n == 0:
            return []
        ans = []
        backtrack(0,[],ans)       
        return ans
    
    def backtrack(row, qList, ans):
        
        if row == N:                        #當列數等於N             
            ans.append(["-"*x + "Q" + "-"*(N-1-x) for x in qList])      #印出此組解
            return 
        
        for col in range(N):                            #當列數小於N
            if promising(col, row, qList):              #判斷此位置是否為promising
                backtrack(row+1, qList+[col], ans)      #若是，則往下一列搜尋                   
                
    def promising(col, row, qList):       
        for r in range (row):                            #目前位置與第0列的Q做比對，一直比到目前列數的前一列的Q
            if qList[r] == col or row-r == abs(col-qList[r]):       #若不符合(兩個Q在同行或同一條斜線)
                return False                
        return True
   
    return NQueens(N)
    
if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    