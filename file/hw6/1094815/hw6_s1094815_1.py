def homework_6(nodes):
    # 使用 Kruskal Algorithms

    # 計算距離
    def distance(i, j):
        return abs(i[0]-j[0]) + abs(i[1]-j[1])

    # 搜尋並查集內 x 的 root
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # 結點的總數
    n = len(nodes)
    # 並查集 hash (初始化所有結點的 parent 為自己)
    parent = {node:node for node in range(n)}
    # 將所有 edge 以距離為基準從小到大排序，log 內部元素結構為 (node1, node2, distance)
    log = sorted([(i, j, distance(nodes[i], nodes[j]))  for i in range(n-1)  for j in range(i+1, n)], key = lambda x:x[2])

    ans = 0
    for node1, node2, weight in log:
        root1, root2 = find(node1), find(node2)
        if root1 != root2: # 若 node1 與 node2 的 root 不相同，代表兩者不在同顆樹內
            parent[root1] = root2 # 則 union 兩棵樹
            ans += weight # 增加總距離
        # p.s. 若兩者 root 相同，代表他們已經被並入同棵樹，則不進行合併，繼續迭代下個 edge
    return ans