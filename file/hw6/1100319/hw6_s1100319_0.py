def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    W = [[0]*(len(nodes))for i in range(len(nodes))]    #建立矩陣W
    
    for i in range(len(nodes)-1):                       
        for j in range(i+1,len(nodes)):
            W[i][j] = W[j][i] = abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])   #將相鄰兩點的權重填入矩陣W

    F = []                             #建立一個空陣列F，用來存放取到的邊的權重
    nearest = [0]*len(nodes)           #建立nearest陣列，用來存放距離Vi最近的頂點的索引值
    distance = [0]*len(nodes)          #建立distance陣列，用來存放Vi與Vnearest[i] 之間的邊的權重
    for i in range(1,len(nodes)) :     #將兩陣列初始化
        nearest[i] = 0                 
        distance[i] = W[0][i]

    n = 1
    while n <= len(nodes)-1:           
        min = float("inf")
        for i in range(1,len(nodes)):   #尋找 distance[i] 當中最小非負值的索引值 i
            if 0 <= distance[i] and distance[i]< min:
                min = distance[i]
                vnear = i

        e = distance[vnear]             #找到的最小權重
        F.append(e)                     #加到陣列F中
        distance[vnear]  = -1           #將其權重改設為-1
        for i in range (1,len(nodes)):          #根據找到的新頂點，更新兩個陣列
            if distance[i] == -1:               #若權重為-1則continue
                continue
            if W[i][vnear] < distance[i]:       #若加入的新頂點能使原來的權重變小
                distance[i] = W[i][vnear]       #distance[i]更新為此權重
                nearest[i] = vnear              #nearest[i]更新為新頂點
    
        n +=1         

    total = sum(F)    
    return total

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    