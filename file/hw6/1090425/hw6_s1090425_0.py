def homework_6(nodes): 
    l = len(nodes)                                                               #總節點數量
    W = [[0]*l for row in range(l)]                                              #初始化相鄰矩陣
    for i in range(l-1):                                                         #從第一個節點開始分別與比自己後面的節點計算距離
        j = l-i
        for k in range(1,j):                                      
            edge = abs(nodes[i][0]-nodes[i+k][0])+abs(nodes[i][1]-nodes[i+k][1]) 
            k=k+i
            W[i][k]=edge                                                         #因為是無向圖所以對稱
            W[k][i]=edge


    visited_node = [0]*l                                                        #紀錄走訪節點情形              
    no_edge = 0
    visited_node[0] = True                                                      #判斷是否走訪過
    sum = 0                                                                     #計算最小生成樹的所有邊的權重總和
    inf = float("inf")
    while no_edge < l-1:                                                        #總共會選出l-1個邊
        minimum = inf
        a = 0
        b = 0
        for m in range(l):
            if visited_node[m]:                                             
                for n in range(l):
                    if ((not visited_node[n]) and W[m][n]):  
                        if minimum > W[m][n]:
                            minimum = W[m][n]
                            a = m
                            b = n

        sum += W[a][b]
        visited_node[b] = True
        no_edge += 1


    return sum

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    