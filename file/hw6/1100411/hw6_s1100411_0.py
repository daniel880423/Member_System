def homework_6(nodes): 
    # 請使用 Prim Algorithms / Kruskal Algorithms
    dist = {}
    n = len(nodes)
    for i in range(n):
        dist[nodes[i][0], nodes[i][1]] = float("inf") if i else 0 #[0,0]的距離為零 可先排除
    res = 0
    while dist:
        k = float("inf")
        for i in dist:
            if dist[i] <= k: #找出最短距離
                k = dist[i]
                x, y = i[0], i[1] 
        res += dist.pop((x,y)) #加上之後移除繼續下一個資料
        for i in dist:
            k = (abs(x-i[0])+abs(y-i[1]))
            if k < dist[i]:
                dist[i] = k
    return res

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    