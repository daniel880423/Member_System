def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    D = [[101] * total for row in range(total)]
    P = [[-1] * total for row in range(total)]
    homework_5.traval = ""
    pathnums = len(matrix)
    for i in range(pathnums):
       D[matrix[i][0]-1][matrix[i][1]-1] = matrix[i][2]
       
    for i in range(total): 
        for j in range(total):
            for k in range(total):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k 
            
    if P[start-1][end-1] == -1:
        return [-1,None]
   
    '''return P'''

    return [D[start-1][end-1],str(start)+Path(start,end,P)+str(end)]

def Path(start,end,P):
    if P[start-1][end-1] != -1:
        Path(start,P[start-1][end-1],P)
        homework_5.traval = homework_5.traval + str(P[start-1][end-1]+1)
        Path(P[start-1][end-1],end,P)
    return homework_5.traval

if __name__ == '__main__':
    matrix = [[1, 2, 4], [1, 3, 5], [2, 6, 1], [3, 4, 4], [3, 1, 1], [4, 5, 2], [5, 6, 1], [6, 7, 10]]
    start = 3;end = 6; total = 8
    print(homework_5(matrix, start, end, total))
    