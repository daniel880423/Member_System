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

    n = len(nodes) # 結點的總數
    parent = {node:node for node in range(n)} # 並查集 hash (初始化所有結點的 parent 為自己)
    log = sorted([(i, j, distance(nodes[i], nodes[j])) for i in range(n-1) for j in range(i+1, n)], key = lambda x:x[2])

    ans = 0
    added = set()
    for node1, node2, weight in log:
        if len(added) == n:
            return ans
        root1, root2 = find(node1), find(node2)
        if root1 != root2:
            added |= {node1, node2}
            parent[root1] = root2
            ans += weight
    return ans