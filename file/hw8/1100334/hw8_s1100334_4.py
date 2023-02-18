def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    def queens(col, dif, sum):
        p = len(col)
        if p==N and N!=0:
            ans.append(col)

        for q in range(N):
            if q not in col and p-q not in dif and p+q not in sum: 
                queens(col+[q], dif+[p-q], sum+[p+q])  
    
    ans=[]
    queens([],[],[])
    for i in range(len(ans)):
        for j in range(N):
            s="-"*ans[i][j] + "Q" + "-"*(N-ans[i][j]-1)
            ans[i][j]=s

        
    return ans



if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    