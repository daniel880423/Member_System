def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    ans=[]
    def queens(i):
        if promising(i):         
            if i+1 == N:
                printing()                      
            else:
                for j in range (N):
                    col[i+1]=j
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
        for n in col: ##
            term="" 
            for m in range(N):
                if n!=m:
                    term+="-"
                else:
                    term+="Q"
            A.append(term)
        ans.append(A)


      
    col=[None for i in range (N)]       
    for i in range (N):
        col[0] = i
        queens(0)


    return ans

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    