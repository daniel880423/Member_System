def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    length = len(matrix)
    
    m = []
    for i in range(total):
        l = []
        for j in range(total):
            l.append(float('inf'))
        l[i] = 0   
        m.append(l)
    for k in range(length):    
        m[matrix[k][0]-1][matrix[k][1]-1] = matrix[k][2]
        
    p = []
    for i in range(total):
        l = []
        for j in range(total):
            l.append(-1)         
        p.append(l)
    
       
    for k in range(length):    
        m[matrix[k][0]-1][matrix[k][1]-1] = matrix[k][2]
                   
    A = m
    
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if A[i][k]+A[k][j] < A[i][j]:
                    A[i][j] =  A[i][k]+A[k][j] 
                    p[i][j] = k 

    print(p)

    if m[start-1][end-1] == float('inf'):
        return[-1, None]    
    if m[start-1][end-1] == 0:
        return[0, None]
    print(A)
    
    global a
    a = str(start)    
    def  getpath(i, j):
        
        if p[i][j]!=-1:            
            getpath(i, p[i][j])
            b = str(p[i][j]+1)
            global a
            a = a+b
            
            getpath(p[i][j],j)
            
    
    
    getpath(start-1, end-1)
    a= a + str(end)
    return [A[start-1][end-1], a]



if __name__ == '__main__':
    matrix =  [[2, 1, 6], [2, 3, 8]]
    start = 2;end = 2; total = 3
    print(homework_5(matrix, start, end, total))
    