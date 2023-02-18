def homework_8(N):
    if N == 0:return []
    arc= (queen(N,()))                                                
    lst = []                                                          
    for i in arc:                                                     
        ans = []                                                        
        for j in i:                                                     
            queens=""
            for k in range(N):                                          
                if j !=k:                                              
                    queens += "-"
                else:                                                  
                    queens += "Q"
            ans.append(queens)                                         
        lst.append(ans)                                               
    return lst        
def conflict(state,nextX):
    ney = len(state)
    if any(abs(state[i]-nextX)==0 for i in range(len(state))):          
        return True
    if any(abs(state[i]-nextX)== ney-i for i in range(len(state))):   
        return True
    return False
def queen (n,state):
    if len(state) == n:                                                
        return[()]
    ans = []
    for pos in range(n):
        if not conflict(state,pos):                                     
            ans += [(pos,)+ result for result in queen(n,state+(pos,))]
    return ans
if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    