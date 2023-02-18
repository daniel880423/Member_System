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

    #A是一個list用來存取path矩陣中的距離，利用二維矩陣表達(如[[起點, 終點, 兩點距離],...])
    #當起點和終點不同時才需要存取距離 
        A=[]
        for i in range(num_node):
            for j in range(num_node):
                if i != j:
                    A.append([i, j, path[i][j]])

    #外圍while迴圈終止條件為已拜訪的節點總數等於總節點個數  #min_path代表最小距離
    #第一個for迴圈跑已拜訪過之節點也就是起點(從第0個節點開始)，第二個for迴圈跑A list中之每一個index(從0開始)。
    #A[j][0]代表起點，A[j][1]代表終點，A[j][2]為兩點距離，對應到A list中每一個二維index的 0 1 2。
    #當目前拜訪的節點和A[j][0]相同並且A[j][1]還沒被拜訪過，如果A[j][2]小於min_path(無限大)，把min_path設為A[j][2]，新拜訪的節點new為A[j][1]。
    #內部for迴圈跑完後，將new存進visit，sum和min_path相加，接著再跑下一次while迴圈。
        while len(visit) != num_node:
            min_path = float('inf')
            for i in range(len(visit)):
                for j in range(len(A)):
                    if visit[i] == A[j][0] and A[j][1] not in visit:
                        if A[j][2] < min_path:
                            min_path = A[j][2]
                            new = A[j][1]
            visit.append(new)
            sum += min_path

    return sum  #回傳最短距離

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    