def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    W = [[float("inf")]*len(nodes) for i in range (len(nodes))]    #設一個全為inf的矩陣，矩陣大小為節點個數*節點個數
    #以下for迴圈為添加節點對節點的距離
    for i in range(len(nodes)):
        for j in range(i,len(nodes)):#只需要跑上半矩陣(因為矩陣為對角線對稱)
            W[j][i] = W[i][j] = abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])#將距離填入對應位置(上半=下半(只需i,j互換))
    ans = 0                     #將答案設為0                            
    nearest = [0]*len(nodes)    #設一個nearest陣列，初始值全設0
    distance = [0]*len(nodes)   #設一個distance陣列，初始值全設0

    #F = []                      #F設為空陣列

    #以下為修改nearest、distance 的初始值
    for i1 in range(1,len(nodes)):  # i1 從 1 ~ 節點個數-1  
        nearest[i1] = 0             #nearest[i1]皆為0，因為一開始只能連第0個節點
        distance[i1] = W[0][i1]     #distance[i1] 設為第i1個節點到第0個節點的距離(其距離值可從相鄰矩陣W獲得)
    
    for n in range(len(nodes)-1):       #n只是用來判斷要做幾次而已，其值用不到
        min_n = float("inf")            #將min_n設為無限
        #以下迴圈用來找離最近的節點編號以及距離值
        for i2 in range(1,len(nodes)):  # i2 從 1 ~ 節點個數-1
            if 0<=distance[i2] and distance[i2]<min_n:  # 如果min_n > distance[i2] >= 0
                min_n = distance[i2]                    # min_n改為distance[i2](最短距離)
                vnear = i2                              # 最近的節點 = 第i2個節點(最近節點編號)
                                              
        #e = [nearest[vnear],vnear]
        ans+=W[nearest[vnear]][vnear]                   #ans加上離最近的節點的距離(其距離值可從相鄰矩陣W獲得)
        #F.append(e)
        distance[vnear] = -1                            #離最近的節點的距離設成-1，之後就不用考慮這個節點了

        #以下為修改nearest、distance 的值(因為參考節點多加了第vnear個節點)
        for i3 in range(1,len(nodes)):                  # i3 從 1 ~ 節點個數-1
            if W[vnear][i3]<distance[i3]:               # 如果W[vnear][i3](第i3個節點到新的參考節點(vnear)的距離) < distance[i3](第i3個節點的初始距離)
                distance[i3] = W[vnear][i3]             # distance[i3] 改為 W[vnear][i3](第i3個節點到新的參考節點(vnear)的距離)
                nearest[i3] = vnear                     # 離第i3個節點最近的節點就會修改成vnear

    return ans                                          #回傳答案

if __name__ == '__main__':
    nodes = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(homework_6(nodes))
    # 22
    