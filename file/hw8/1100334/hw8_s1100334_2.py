def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    ans=[]
    def queens(i):
        for j in range(N):
            col[i]=j
            if promising(i):         
                if i+1 == N:
                    printing()                      
                else:
                    queens(i+1)

    def promising(i):
        k=0
        switch=1
        while (k<i) and (switch):
            if (col[i]==col[k]) or (abs(col[i]-col[k])==i-k):
                switch=0
            k+=1
        return switch

    def printing():
        A=[]
        for i in range(N):
                s = '-' * col[i] + 'Q' * 1 + '-' * (N-col[i]-1)
                A.append(s)   
        ans.append(A)

  
    col=[None for i in range (N)]       
    queens(0)


    return ans

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    