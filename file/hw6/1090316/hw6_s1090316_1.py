import numpy as np
def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 使用 Prim Algorithm
    V = len(nodes)   #總共有V個點
    INF = 9999999    
    sum=0            #最短距離初始值為0
    selected = np.linspace(0,0,100) #建立一個空矩陣
    c = 0   #邊的數目初始值為0，總共會有V-1個邊
   
    selected[0] = True
    d = [[float("INF")]*V for i in range(V)] #列出各點之間之距離
    for i in range(V):
        for j in range(V):
            if i==j:     #i=j代表是同一個座標
                continue  #跳過，不計算
            if i!=j:
                d[i][j]=abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1]) #nodes之間的距離

    
    
    while (c < V - 1): #如果邊常數目沒有大於V-1就繼續迴圈 
        minimum = INF  #設最小值
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and d[i][j]):  
                        # not in selected and there is an edge
                        if minimum > d[i][j]:
                            minimum = d[i][j]
                            x = i
                            y = j
        sum+=d[x][y]
        selected[y] = True
        c += 1
    return sum
    

if __name__ == '__main__':
    nodes = [[-1, 8], [1, 9], [-3, -8], [-7, 0], [15, 2], [0, -9]]
    print(homework_6(nodes))
    # 22
    