def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    col=[-1]*N
    t_arr=[]   
    for i in range(N):
        flag=True
        col=[-1]*N
        arr=["-"*N for s in range(N)]
        col[0]=i
       
        a=queens(0,col,N,arr)
        for j in range(N):
            if (a[j]=="-"*N):
                flag=False
                break
        if (flag):    
            t_arr.append(a)
    return t_arr


def queens (i,col,N,arr):
    if (promising(i,col,N,arr)):
        arr[i]=col[i]*'-'+'Q'+(N-1-col[i])*'-'
        if (i==N-1):
            return arr
        else:
            for j in range(N):
                col[i+1]=j
                queens(i+1,col,N,arr)    
    return arr       
def promising (i,col,N,arr):
    k=0
    switch=True
    while (k<i and switch==True):
        if (col[i]==col[k] or (abs(col[i]-col[k])==(i-k))):
            switch=False
        k+=1
    return switch
if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    