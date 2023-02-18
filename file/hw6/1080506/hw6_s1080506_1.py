def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    V = list(range(len(nodes))) #所有頂點的集合
    V = set(V)
    visit = {0} #存取已經讀取的點
    sum = 0 #計算最短路徑
    weight = [[float("inf")]*len(nodes) for i in range(len(nodes))] #定義權重矩陣
    for i in range(len(nodes)): #把兩點距離放入權重矩陣
        for j in range(i+1,len(nodes)):
            weight[i][j] = abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])
            weight[j][i] = abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])
    
    for i in range(1,len(nodes)):
        sum = get_smallest_distant(visit,weight,V,sum)
    
    return sum
def get_smallest_distant(visit,weight,V,sum):
    mini = 400
    for i in visit:
        for j in (V-visit):
            if weight[i][j]<mini:
                mini = weight[i][j]
    sum+=mini
    visit.add(j)

    return sum

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    