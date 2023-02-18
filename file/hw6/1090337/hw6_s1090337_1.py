def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    #使用 Prim Algorithms
    r=[]    #路徑長矩陣
    if len(nodes)>=1 and len(nodes)<=100:   #防呆
        for i in range(len(nodes)):#建立矩陣
            r.append([])
            if len(nodes[i])==2:    #防呆
                for j in range(len(nodes)):
                    if i==j:
                        r[i].append(float('inf'))   #去除自己到自己的路徑長
                    else:
                        if nodes[j][0]==nodes[i][0] and nodes[j][1]==nodes[i][1] and nodes[i][0]>=-100 and nodes[i][1]<=100:
                            print('error')#防呆
                            return
                        else:
                            n=abs(nodes[j][0]-nodes[i][0])+abs(nodes[j][1]-nodes[i][1])#路徑長
                            r[i].append(n)
            else:
                print('error')
                return
    else:
        print('error')
        return
    #print(r)
    p=[0]   #記錄點list
    ans=0
    while(True):    #使用 Prim Algorithms
        w=float('inf')
        for i in p:            
            for j in range(len(nodes)):    #提取各點連接路徑長          
                if w > r[i][j]:     #比路徑大小
                    b=[i,j]
                    w=r[i][j]
        r[b[0]][b[1]]=float('inf')    #將已行過的路徑消除     
        if b[1] not in p:    #避免重複
            p.append(b[1])     #紀錄已經過的點
            ans+=w      #輸入路徑長
        if len(p)==len(nodes):
            break       #結束脫離迴圈
    return ans

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    