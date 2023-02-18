def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    D = [[101] * total for row in range(total)]
    P = [[-1] * total for row in range(total)]
    homework_5.traval = ""
    pathnums = len(matrix)
    for i in range(pathnums):
       D[matrix[i][0]-1][matrix[i][1]-1] = matrix[i][2]
       
    for k in range(total): 
        for i in range(total):
            for j in range(total):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k 
            
    if D[start-1][end-1] == 101:
        return [-1,None]

    return [D[start-1][end-1],str(start)+Path(start,end,P)+str(end)]

def Path(start,end,P):
    if P[start-1][end-1] != -1:
        Path(start,P[start-1][end-1],P)
        homework_5.traval = homework_5.traval + str(P[start-1][end-1]+1)
        Path(P[start-1][end-1],end,P)
    return homework_5.traval

if __name__ == '__main__':
    matrix = [[30, 31, 1], [30, 32, 1], [30, 34, 2], [31, 34, 2], [32, 34, 2], [34, 35, 3], [34, 36, 3], [35, 37, 2], [36, 37, 1], [37, 38, 5]]
    start = 30;end = 37; total = 38
    print(homework_5(matrix, start, end, total))
    