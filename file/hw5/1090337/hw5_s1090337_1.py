def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    p=[]#中轉點紀錄
    w=[]#路徑紀錄
    for i in range(total):      #建立中轉點矩陣和路徑矩陣
        p.append([])
        w.append([])
        for j in range(total):
            p[i].append(-1)         
            w[i].append(float('inf'))
            if i==j:
                w[i][j]=0  #相同路徑為零
    n=len(matrix)
    for i in range(n):
        w[matrix[i][0]-1][matrix[i][1]-1]=matrix[i][2]  #輸入相連兩點間路徑
    for k in range(total):      #尋找中轉點
        for i in range(total):
            for j in range(total):
                if w[i][j]>w[i][k]+w[k][j]:
                    p[i][j]=k       #輸入中轉點
                    w[i][j]=w[i][k]+w[k][j]     #輸入路徑
    #print(p)
    #print(w)
    
    s=start-1
    e=end-1
    a=[e]   #紀錄中轉點
    b=str(start) #紀錄路徑順序
    c=0     #路徑長度
    if start != end:        #防呆
        while(True):
            if w[s][e]==float('inf'):       #兩點無路徑相連
                c=-1            
                b=None
                break
            else:
                if s==e:        #檢查完畢
                    #print(b)
                    #print(c)
                    break
                else:
                    if p[s][e]!=-1:     #確認是否有中轉點
                        a.append(p[s][e])
                        e=p[s][e]
                    else:               #兩點間檢查到無中轉點，輸入紀錄
                        c+=w[s][e]              
                        b+=str(e+1)
                        s=e
                        a.pop()
                        if len(a)!=0:
                            e=a[-1]
    else:
        c=-1            
        b=None   
    ans=[c,b]
    return ans

if __name__ == '__main__':
    matrix = [[2, 1, 6], [2, 3, 8]]
    start = 2;end = 2; total = 3
    print(homework_5(matrix, start, end, total))
    