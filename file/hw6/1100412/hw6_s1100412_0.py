def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    len_sum = 0                                                                     #先設立總最短距離為0
    n = len(nodes)                                                                  #設n為nodes長度
    W = [[float("inf")]*n for x in range(n)]                                        #創建一個先都設為無限的n*n矩陣,存取各點間的距離
    for i in range(n):                                                              
        for j in range(n):
            W[i][j] = abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])   #點到點距離公式
    node_queue = [0]                                                                #設一個list:node_queue存走過的node,由第0個node開始
    
    
    for times in range (n-1):                                                       #重複n-1次
        min_distance = float("inf")                                                 #設最短距離為無限
        for k in range(1,n):                                                        #依序判斷未走過的node到已走過的node的距離
            for node in node_queue:                                                 
                if k not in node_queue:                                             #若k是未走過的node
                    if  W[node][k] < min_distance:                                  #若距離比min_distance短
                        nearest = k                                                 #k即為最近的node
                        min_distance=W[node][k]                                     #更新最短距離

        
        node_queue.append(nearest)                                                  #將最近的node加入已走過的node list中
        len_sum += min_distance                                                     #將新的最短距離加入總最短距離中
        
    return len_sum

if __name__ == '__main__':
    nodes =  [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    