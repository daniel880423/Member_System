def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    D = [[1e10 for _ in range(total+1)] for _ in range(total+1)]
    P = [[0 for _ in range(total+1)] for _ in range(total+1)]
    for i in matrix:
        D[i[0]][i[1]]=i[2]
    for i in range(1,total+1):
        D[i][i]=0
  
    
    P_total = [[[0 for _ in range(total+1)]for _ in range(total+1)] for _ in range(total+1)]
    D_total = [[[0 for _ in range(total+1)]for _ in range(total+1)] for _ in range(total+1)]
    D_total[0]=D
    P_total[0]=P
    P_str=""
    
    
  
    for i in range(1,total+1):
        for j in range(1,total+1):
            for k in range(1,total+1):
                if (D_total[i-1][j][k]>D_total[i-1][j][i]+D_total[i-1][i][k]):
                    D_total[i][j][k]=D_total[i-1][j][i]+D_total[i-1][i][k]
                    P_total[i][j][k]=i
                else:
                    D_total[i][j][k]=D_total[i-1][j][k]
                    P_total[i][j][k]=P_total[i-1][j][k]
    
    
          
    if D_total[total][start][end]>5e9:
        return [-1,None]
    else:
        return [D_total[total][start][end],str(start)+path(P_total[total],start,end,P_str)+str(end)]

def path (P,start,end,p_str):
    if (P[start][end]!=0):
        
        p_str+=path(P,start,P[start][end],p_str)
        p_str+=str(P[start][end])
        p_str+=path(P,P[start][end],end,p_str)
        return p_str
    else:
        return ''
if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    
    

    