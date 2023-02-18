
def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    l = len(matrix)
    m = [[float("inf")]*total for _ in range(total)]
    p = [[-1]*total for _ in range(total)] 
    for i in  range(total):
            m[i][i] = 0
    for k in range(l):
        m[matrix[k][0]-1][matrix[k][1]-1] = matrix[k][2]
    
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if m[i][k] + m[k][j] < m[i][j]:
                    m[i][j] = min(m[i][j], m[i][k] + m[k][j])
                    p[i][j] = k
                   
                   
                    


    global strpath
    strpath =str(start)
    def get(a, b):
        if p[a][b]!= -1:
            get(a, p[a][b])
            global strpath            
            strpath = strpath + str(p[a][b]+1)
            get(p[a][b],b)
       
   
    get(start-1, end-1)

    d=m[start-1][end-1]
    
    strpath = strpath + str(end)








    return  [d, strpath]

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    