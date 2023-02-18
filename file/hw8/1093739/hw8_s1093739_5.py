def homework_8(N): 
    
    #建立一個NXN的矩陣
    matrix = [[0 for i in range(N)]for i in range(N)]
    
    
    #判斷皇后是否在同一行或是同一個斜線
    def isvalid(row,col):
        for i in range(row):
            if matrix[i] == col or abs(i-row) == abs(matrix[i]-col):
                return False #在同一行或同一斜線代表nonpromising
            
        return True #不在同一行或同一斜線代表promising

    ans = []#建立答案的List
    
    #利用深度優先走訪與backtracking的遞迴程式來print出答案
    def dfs(row,pre_values):
        if row == N and N != 0: #判斷是否為0矩陣或是最後一列
            ans.append(pre_values)
            return
        for col in range(N):
            if isvalid(row,col):
                matrix[row] = col
                dfs(row+1, pre_values + ["-"*col + "Q" + "-"*(N-col-1)]) #考慮其他種答案後再走訪一次
    dfs(0,[]) #執行深度優先走訪與回溯


    return ans  #回傳最後的解答

if __name__ == '__main__':
    N = 0
    homework_8(N)
  
    