def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
                                           # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    def print_solution(matrix_in):
        for i in range(total):
            for j in range(total):
                if (matrix_in[i][j]) == float('inf'):
                    print("∞", end=" ")
                else:
                    print(matrix_in[i][j], end=" ")
            print(" ")
    len_matrix = len(matrix) 
    
    d = [[float('inf')]*total for _ in range(total)]
    path = [[-1]*total for _ in range(total)]
    print(d)
    print(path)

    for i in range(total):
        for j in range(total):
            if i == j:
                d[i][j] = 0
    
    for k in range(total):
        print("d=",k)
        print_solution(matrix)
        print("path=",k)
        print_solution(path)
        for i in range(total):
            for j in range(total):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                    path[i][j] = k+1
            

    print("d=",total)
    print_solution(matrix)
    print("path=",total)
    print_solution(path)           

    global strpath
    strpath =str(start)
    def get(a, b):
        a=a-1    #注釋此行可得正確p   和p[i][j]必須擇一注釋  
        if p[a][b]!= 0:
            get(a, p[a][b])
            global strpath            
            strpath = strpath + str(p[a][b]+1)
            get(p[a][b],b)
       
    get(start-1, end-1)
    d=m[start-1][end-1]
    strpath = strpath + str(end)
    
    return  [d, strpath]

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    