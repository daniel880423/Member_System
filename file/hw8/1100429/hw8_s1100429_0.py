def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    a = []                                                                        
    for i in que(N):                                                               
        a.append(transferr(i))                                                     
    return a




def quarrel(state, nextX):                                                         
    nextY = len(state)                                                             
    con = any(abs(state[i] - nextX) in (0, nextY - i) for i in range(nextY))       
    return con                                                                     


def transferr(output):                                                             
    vis=['-'*len(output)] * len(output)
    for i ,item in enumerate(output):
        vis[i]=vis[i][:item]+"Q"+vis[i][item+1:]                                   

def que(n, state=()):                                                              
    if len(state) == n:                                                            
        return [()]                                                                
    ans = []
    for pos in range(n):                                                           
        if not quarrel(state, pos):                                               
            ans += [(pos,)+ result for result in que(n, state + (pos,))]          
    return ans

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    