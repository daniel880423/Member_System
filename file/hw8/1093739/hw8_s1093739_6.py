def homework_8(N): 
    
    #建立一個NXN的矩陣
    matrix = [[0 for i in range(N)]for i in range(N)]
    
    
    #判斷皇后是否在同一行或是同一個斜線
   #在同一行或同一斜線代表nonpromising
            
         #不在同一行或同一斜線代表promising

    ans = []#建立答案的List
    
    #利用深度優先走訪與backtracking的遞迴程式來print出答案
    def dfs(row,pre_values,column,slash_left,slash_right):
        if row == N and N != 0: #判斷是否為0矩陣或是最後一列
            ans.append(pre_values)
            return
        
        for col in range(N):
            
            #判斷皇后是否在同一行或是同一個斜線
            if col not in column and row+col not in slash_left and row - col not in slash_right :
                
                dfs(row+1, pre_values + ["-"*col + "Q" + "-"*(N-col-1)],column+[col],slash_left+[row+col],slash_right+[row-col]) #考慮其他種答案後再走訪一次
    dfs(0,[],[],[],[]) #執行深度優先走訪與回溯


    return ans  #回傳最後的解答

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
  
    