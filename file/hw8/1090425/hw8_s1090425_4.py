def homework_8(N):
    global result 
    result = []
    DFS(N,[],[],[])                                                     #從0開始深度優先走訪
    ans=[ ["-"*i + "Q" + "-"*(N-i-1) for i in sol] for sol in result]
    if ans==[[]]:                                                       #無解
        ans=[]
    return ans

def DFS(n,queens, slash_r, slash_l):                                   #深度優先走訪
    global result                              
    row = len(queens)
    if row==n:                                                         #紀錄找到的解
        result.append(queens)
        return None                         
    for col in range(n):                                                  
        if col not in queens and row-col not in slash_r and row+col not in slash_l: #判斷皇后有沒有被攻擊
            DFS(n,queens+[col], slash_r+[row-col], slash_l+[row+col])                 
    
if __name__ == '__main__':
    N=1
    print(homework_8(N))
    
