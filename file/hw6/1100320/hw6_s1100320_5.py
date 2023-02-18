from math import inf
def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    sum = 0 #sum用來存取經過各點之最短距離                                                               
    visit = [0] #visit為一個list存取已拜訪過的節點
    num_node = len(nodes)   #num_node表示節點總數
    path = [[float('inf')for i in range(num_node)]for j in range(num_node)] #path為二維矩陣存取每一點到另外一點的距離

    #建立path矩陣，對角線元素皆是無限大，非對角線元素為兩點座標x,y分別相減取絕對值再相加，並且矩陣元素對稱於對角線。
    if num_node <= 100:
        for i in range(num_node):
            for j in range(num_node):
                if i != j:
                    path[i][j] = abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
                    path[j][i] = path[i][j]

   
    #外圍while迴圈終止條件為已拜訪的節點總數等於總節點個數  #min_path代表最小距離
    #兩個for迴圈代表path矩陣的列跟行(i,j從0開始)
    #當目前拜訪的節點和i相同並且j還沒被拜訪過，如果path[i][j]小於min_path(無限大)，把min_path設為path[i][j]，新拜訪的節點new為j。
    #內部for迴圈跑完後，將new存進visit，sum和min_path相加，接著再跑下一次while迴圈。
        while len(visit) != num_node:
            min_path = float('inf')
            for i in range(num_node):
                for j in range(num_node):
                    if i in visit and j not in visit:
                        if path[i][j] < min_path:
                            min_path = path[i][j]
                            new = j
            visit.append(new)
            sum += min_path

    return sum  #回傳最短距離

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    