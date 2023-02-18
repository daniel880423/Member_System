def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    #matrix = [[1,2,1],[1,3,1],[3,4,1]]
#total = 4
# A = np.zeros([4,4])
    W = [[float('inf') for i in range(total)] for j in range(total)]
    for i in range(0, total):
        for j in range(0, total):
    		    if i==j:
			        W[i][j]=0
#設定相鄰矩陣            
    for i in range(len(matrix)):
        W[matrix[i][0]-1][matrix[i][1]-1] = matrix[i][2]

#設定中轉點path
    path =  [[-1 for i in range(total)] for j in range(total)]
#path = np.zeros([total,total])
    A = W   
#替換矩陣路徑距離
    for k in range(0,4):
        for i in range(0,4):
            for j in range(1,4):
                if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = min(A[i][j],A[i][k]+A[k][j])
                    path[i][j] = k

    global s
    s = str()
    s+=str(start)
    if A[start-1][end-1] == float("inf") or start == end : 
        return [-1,None]
    
    def getpath(i,j,path):
        global s
        if(path[i][j] != -1):
            getpath(i,path[i][j],path)
            s += str(path[i][j]+1)
            #print(str(i+1)+str(j)+str(end))
            getpath(path[i][j],j,path)
    getpath(start-1,end-1,path)
    s+=str(end)
    return [A[start-1][end-1], s]
                     
#print(path)
#print(W[0][3])
#print(s)
if __name__ == '__main__':
    matrix = [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2;end = 2; total = 5
    print(homework_5(matrix, start, end, total))
    