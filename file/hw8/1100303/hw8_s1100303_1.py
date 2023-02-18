def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    ans=[]
    now=[['-']*N for i in range(N)]
    right=[]
    left=[]
    column=[]

    if N<=0:
        return ans
    
    def dfs(now,row):
        if row>=N:
            current=[''.join(row) for row in now]
            ans.append(current)

        for col in range(N):
            a=row+col
            b=row-col
            if(a not in right) and (b not in left) and (col not in column) :
                now[row][col]='Q'
                right.append(a)
                left.append(b)
                column.append(col)

                dfs(now,row+1)
                
                now[row][col]='-'
                right.remove(a)
                left.remove(b)
                column.remove(col)
                
    dfs(now,0)
    return ans

if __name__ == '__main__':
    N = 0
    print(homework_8(N))
    # [["Q"]]
    