def homework_8(N): 
    #建立一個NXN的矩陣
    matrix = [[0 for i in range(N)]for i in range(N)]
    
    #判斷是否為0矩陣
    if N == 0:
        return []
    #判斷皇后是否在同一行或是同一個斜線
    def isvalid(i,j):
        for row in range(i):
            if matrix[row] == j or abs(row-i) == abs(matrix[row]-j):
                return False #在同一行或同一斜線代表nonpromising
            
        return True #不在同一行或同一斜線代表promising

    ans = []#建立答案的List
    
    #利用深度優先走訪與backtracking的遞迴程式來print出答案
    def dfs(i,pre_values):
        if i == N:
            ans.append(pre_values)
            return
        for j in range(N):
            if isvalid(i,j):
                matrix[i] = j
                dfs(i+1, pre_values + ["-"*j + "Q" + "-"*(N-j-1)]) #考慮其他種答案後再走訪一次
    dfs(0,[]) #執行深度優先走訪與回溯


    return ans #回傳最後的解答

if __name__ == '__main__':
    N = 0
    print(homework_8(N))
  
    