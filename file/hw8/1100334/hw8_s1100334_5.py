def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    def queens(col, rslash, lslash):
        r = len(col)
        if r==N and N!=0:
            ans.append(col)

        for c in range(N):
            if c not in col and r-c not in rslash and r+c not in lslash: 
                queens(col+[c], rslash+[r-c], lslash+[r+c])  
    
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
    