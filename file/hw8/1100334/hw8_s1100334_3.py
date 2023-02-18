def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    ans=[]
    def queens(i):
        for j in range(N):
            col[i]=j
            if promising(i):
                if i+1==N:
                    A=[]
                    for n in range(N):
                        s = '-' * col[n] + 'Q'*1 + '-' * (N-col[n]-1)
                        A.append(s)   
                    ans.append(A)
                else:
                    queens(i+1)


    def promising(i):
        for k in range(i):
            if (col[i]==col[k]) or (abs(col[i]-col[k])==i-k):
                return 0
        return 1
  
    col=[-1]*N       
    queens(0)


    return ans

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    