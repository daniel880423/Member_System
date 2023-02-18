def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    def listback():
        r=[]    #基底矩陣
        for i in range(N):#建立矩陣
            r.append([])
            for j in range(N):
                r[i].append(float('inf'))
        #print(r)
        return r
    l=listback() #獲取基礎的list
    d=[-1,-1] 
    count=0     #執行次數
    n=0 #Q數量
    a=[[0],[count],[-count],[count]] #行列與斜線的紀錄
    ans=[]
    z=-1
    while True:     #迴圈
        if count < N:         
            for i in range(N):#建立矩陣
                c=0     #處理返回上層
                for j in range(N):
                    if i in a[0]:
                        if i==0 :
                            if j != count: #行輸入
                                l[i][j]="-"
                            else:
                                l[i][j]="Q"
                                d[0]=(i)
                                d[1]=(j)
                                n+=1
                        else:
                            l[i][j]="-"
                            c+=1
                    else:
                        if j in a[1]:  #列輸入
                            l[i][j]="-"
                            c+=1
                        else:
                            if (i-j) in a[2]:# 斜線處理
                                l[i][j]="-"
                                c+=1
                            elif (i+j) in a[3]:
                                l[i][j]="-"
                                c+=1
                            else:
                                l[i][j]="Q" #可輸入Q者輸入Q
                                d[0]=i
                                d[1]=j                                                         
                                a[0].append(i)
                                a[1].append(j)
                                a[2].append(i-j)
                                a[3].append(i+j)
                                n+=1
                    if c==N:        #處理返回上層情況
                        a[1]=a[1][:-1]
                        a[2]=a[2][:-1]
                        a[3]=a[3][:-1]
                        n-=1
                        while True:     
                            if c==N:
                                if d[1]!=N-1:
                                    
                                    l[d[0]][d[1]]="-"   #清除原先Q位置
                                    d[1]=d[1]+1
                                    if d[1] not in a[1] and (d[0]-d[1]) not in a[2] and (d[0]+d[1]) not in a[3]:
                                        l[d[0]][d[1]]="Q"   #更新Q
                                        c=0 
                                        a[1].append(d[1])
                                        a[2].append(d[0]-d[1])
                                        a[3].append(d[0]+d[1])
                                        i=d[0]+1
                                        n+=1
                                        for k in range(N):  #重新處理原來層
                                            if i in a[0]:                            
                                                l[i][k]="-"
                                                c+=1
                                            else:
                                                if k in a[1]:
                                                    l[i][k]="-"
                                                    c+=1
                                                else:
                                                    if (i-k) in a[2]:
                                                        l[i][k]="-"
                                                        c+=1
                                                    elif (i+k) in a[3]:
                                                        l[i][k]="-"
                                                        c+=1
                                                    else:
                                                        l[i][k]="Q"
                                                        d[0]=i
                                                        d[1]=k
                                                        a[0].append(i)
                                                        a[1].append(k)
                                                        a[2].append(i-k)
                                                        a[3].append(i+k)
                                                        n+=1   
                                else:
                                    c=0
                                    break
                            else:
                                c=0
                                break   
            count=count+1 
            
            if n==N:       #矩陣轉字串
                z+=1
                ans.append([])
                for i in range(N):
                    s=str()    
                    for j in range(N):  
                        s=s+str(l[i][j])
                    ans[z].append(s)
            a=[[0],[count],[-count],[count]]    #初始化
            n=0
            l=listback() 
        else:
            count=0
            break
    #print(ans)
    return ans
if __name__ == '__main__':
    N = 7
    print(homework_8(N))
    # [["Q"]]
    