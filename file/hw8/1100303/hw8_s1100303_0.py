def place(t):
    for i in range(1,t):
        if t-1==abs(x[t]-x[i]):
            return False
    return True

def dfs(t):
    global ans
    if t>N:
        sol=[]
        for i in range(1,N+1):
            temp=''
            for j in range(1,N+1):
                if j==x[i]:
                    temp+='Q'
                else:
                    temp+='-'
            sol.append(temp)
        result.append(sol)
    else:
        for i in range(t,N+1):
            x[t],x[i]=x[i],x[t]
            if place(t):dfs(t+1)
            x[t],x[i]=x[i],x[t]

def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    global x
    global result
    result=[]
    x=[i for i in range(N+1)]
    dfs(1)
    return result


            






   

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    