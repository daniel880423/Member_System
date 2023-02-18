def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    
    class Solution(object):
        def solveNQueens(self, n):
            def dfs(col,vals):
                if col==n: #每行都run好了
                    res.append(vals)
                    return 
                curStr='-'*n
                for row in range(n): #決定row的位置
                     if check(col,row): #查看是否可以放置
                        board[col]=row
                        #遞迴決定下一行
                        dfs(col+1,vals+[ curStr[:row]+'Q'+curStr[row+1:] ])
        
            def check(col,row):
                for pos in range(col): #看先前的其他行是否已經有人 列與當前row相等    
                    #若有哪列已經與row相等 or 斜對角相等 則false
                    if board[pos]==row or abs(col-pos)==abs(row-board[pos]):
                        return False
                return True
            
            board=[-1]*n #board[x]=y : 第x行、第y列中放置queen
            res=[]
            dfs(0,[])
            return res
        
    result=Solution()
    ans=result.solveNQueens(N)
    return ans

    
        
    

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    