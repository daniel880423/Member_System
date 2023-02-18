def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms

    W = [[0] * len(nodes) for i in range(len(nodes))] #生成一個全為0的相鄰矩陣(節點的順序按照輸入的nodes)
    for i in range(len(nodes)): #將所有節點之間的距離輸入相鄰矩陣
        for j in range(len(nodes)):
            if i == j:
                continue
            W[i][j] = abs(nodes[j][0]-nodes[i][0]) + abs(nodes[j][1]-nodes[i][1])

    sum = 0 #最短距離初始化為0
    visit = [0] #初始化一個由節點0為第一項的visit list
    while(len(visit) != len(nodes)): #當visit list長度不等於節點數時執行
        min = 0 #邊的最小值初始化為0
        for a in range(len(visit)): #依照目前visit中的節點依序當作i

            i = visit[a]

            for j in range(len(nodes)): #根據節點i尋找最短路徑，以及最短路徑所到達的節點

                if W[i][j] == -1 or W[i][j] == 0: #如果相鄰矩陣中該項為0或-1(代表終點是自己，或者已經選擇過)則跳過此次迴圈
                    continue

                if min == 0: #如果是第一個值，則直接假設成最小值
                    if j in visit: #如果當前的節點已經在visit list中，則跳過此次迴圈
                        continue
                    min = W[i][j] 
                    M = j
                    I = i


                elif W[i][j] < min: #如果比最小值小，則取代為最小值
                    if j in visit:
                        continue
                    min = W[i][j]
                    M = j
                    I = i
        sum += min #最短距離總和加上目前所選到的邊的距離
        visit.insert(len(visit), M) #將目前的節點加入visit list
        W[I][M] = -1 #將此邊的長度設為-1代表已選過
        W[M][I] = -1 #將此邊的長度設為-1代表已選過



    return sum #回傳最短距離

if __name__ == '__main__':
    nodes = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(homework_6(nodes))
    # 22
    