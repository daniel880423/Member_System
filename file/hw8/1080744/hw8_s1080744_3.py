def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    col=[-1]*N
    t_arr=[]   
    f_arr=[]
    for i in range(N):
        flag=True
        col=[-1]*N
        arr=["-"*N for s in range(N)]
        col[0]=i
       
        
       
        
        a=queens(0,col,N,arr,f_arr)
        # print(f_arr)
        # print("=======================")
        #t_arr.append(a)
        
        # for j in range(N):
        #     if (a[j]=="-"*N):
        #         flag=False
        #         break
        # if (flag):    
        #     t_arr.append(a)
    return f_arr


def queens (i,col,N,arr,f_arr):
    if (promising(i,col,N,arr)):
        
        arr[i]=col[i]*'-'+'Q'+(N-1-col[i])*'-'
       # print(i==N-1)
        if (i==N-1):
        
 #           print("=====================")
#            print(arr)
            f_arr.append(arr)
            return arr
        else:
            for j in range(N):
               # print(j)
                
                col[i+1]=j
#                print(i+1)
                queens(i+1,col,N,arr,f_arr) 
                
            return arr
        
#    print(i,col[i],"x")

#    print("+++++++++++++++++++++")
   # print(arr)
    return arr


      
def promising (i,col,N,arr):
    k=0
    switch=True
    while (k<i and switch==True):
        if (col[i]==col[k] or (abs(col[i]-col[k])==abs(i-k))):
            switch=False
        k+=1
    return switch
if __name__ == '__main__':
    N = 2
    print(homework_8(N))
    # [["Q"]]
    