def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    llone=[]
    lltwo=[]
    total+=1
    ans=""
    for  i in range(0,total):
        tempone=[]
        temptwo=[]
        for  j in range(0,total):
            tempone.append(0xc48763)
            temptwo.append(j)
        llone.append(tempone)
        lltwo.append(temptwo)
    for vec in matrix:
        llone[vec[0]][vec[1]]=vec[2]
    for k in range(0,total):
        for i in range(0,total):
            for j in range(0,total):
                if(llone[i][k]+llone[k][j]<llone[i][j]):
                    llone[i][j]=llone[i][k]+llone[k][j]
                    lltwo[i][j]=lltwo[i][k]

    def find_path(ans,s,e):
        ans+=str(s)
        if(s!=e):
            return find_path(ans,lltwo[s][e],e)
        else:
            return ans
    ans = find_path(ans,start,end)
    if(llone[start][end]%0xc48763==0):
        return [-1,None]
    else:
        return [llone[start][end],ans]







if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    