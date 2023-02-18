def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    Output=[]    #最後印出的結果矩陣[步數,經過的所有點]
    step=0       #步數初始值為0
    
    for i in matrix:
        for j in matrix:
            if (matrix[i][0]!= start and matrix[j][1]!= end):    #如果矩陣第一個值都沒有等於start/第二個值沒有等於end，代表start無法到達end
                step=-1                          #步數顯示為-1
                Output=[step,None]
            else:
                break
    for k in matrix:
        for h in matrix:
            if(matrix[k][1]==end):     
                a=matrix[k][0]
                step+=matrix[k][2]
                if(a==matrix[h][1] and start==matrix[h][0]):
                    step+= matrix[h][2]                
                    Output=[step,start, a, end]

            else:
                k+=1

            
    return Output
    
if __name__ == '__main__':
    matrix = [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2;end = 4; total = 5
    print(homework_5(matrix, start, end, total))