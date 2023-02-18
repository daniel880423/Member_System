def homework_8(N): 
    
    
    ini = [[0 for i in range(N)]for i in range(N)]
    
    
    
    def isvalid(row,col):
        for i in range(row):
            if ini[i] == col or abs(i-row) == abs(ini[i]-col):
                return False 
            
        return True 

    ans = []
    
    
    def define(row,pre):
        if row == N and N != 0: 
            ans.append(pre)
            return
        for col in range(N):
            if isvalid(row,col):
                ini[row] = col
                define(row+1, pre + ["-"*col + "Q" + "-"*(N-col-1)]) 
    define(0,[]) 


    return ans  #回傳最後的解答

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
  
    