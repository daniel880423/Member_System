def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    
    inf=float("Inf")
    A=[[inf for a in range(total)] for a in range(total)]#創建矩陣A
    for i in range(total):
        for j in range(total):
            if i==j:
                A[i][j]=0
    path=[[-1 for a in range(total)] for a in range(total)]#創建矩陣path

    for i in matrix:
        A[i[0]-1][i[1]-1]=i[2]#在A中放入各點間的距離
    
    for k in range(0,total):#佛洛伊德演算法
        for i in range(0,total):
            for j in range(0,total):
                if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
                    path[i][j] = k+1
    
    p_ans=getpath(path, start-1, end-1,[])
    
    l_ans=A[start-1][end-1]
    if l_ans==inf or l_ans==0:
        l_ans=-1
    if p_ans != []:#將最短路徑改為字串並加上start,end
        p_ans="".join(getpath(path, start-1, end-1,[]))
        p_ans=str(start)+p_ans+str(end)
        return [l_ans,p_ans]
    else :
        return [l_ans,None]
    

    
    

   


def getpath(path,i,j,lst):#遞迴紀錄中轉點
    if path[i][j] != -1:
        getpath(path, i, path[i][j]-1,lst)#檢查start到中轉點之間是否有更多中轉點
        lst.append(str(path[i][j]))
        
        getpath(path, path[i][j]-1, j,lst)#檢查中轉點到end之間是否有更多中轉點
        
    return lst
    
    


if __name__ == '__main__':
    matrix =   [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2;end = 4; total = 5
    print(homework_5(matrix, start, end, total))
    