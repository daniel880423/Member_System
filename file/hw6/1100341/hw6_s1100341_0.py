def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    A = [[float("inf") for i in range(len(nodes))] for j in range(len(nodes))]   #設一個矩陣讓距離都填無限
    # print(A)
    for i in range(len(nodes)):      
        for j in range(len(nodes)):
            A[i][j] = abs(nodes[j][0]-nodes[i][0])+abs(nodes[j][1]-nodes[i][1])  #算出點到點之間的距離
            if i == j:
                A[i][j] = float("inf")                                           #自己到自己的距離設無限
    # for i in A:
    #     print(i)
    visit = [0]
    sum = 0
    while len(visit) < len(nodes):                                               #visit長度等於節點數停止
        min = float("inf")                                                       #設min無限
        for i in visit:                                                          #讓i依序跑找到最小的點的數字
            for j in range(len(nodes)):                                          #j則跑node的長度
                    if A[i][j] < min and j not in visit:                         #如果A[i][j]小於預設min 和j不能找到已經在visit裡面
                        min = A[i][j]                                               
                        a = i                                                    #把找到的i放進暫存的a
                        b = j                                                    #把找到的j放進暫存的b
                        
        visit.append(b)
        # print(A[a][b]) 
        # print(a, b)                                                            #把b加到visit裡面
        sum += min                                                               #min加到sum裡面
        A[a][b] = float("inf")                                                   #把找過的最小改成無限避免重複抓
        A[b][a] = float("inf")
    # for i in A:
    #         print(i)        

   

    return sum

if __name__ == '__main__':
    nodes = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(homework_6(nodes))
    # 20
    