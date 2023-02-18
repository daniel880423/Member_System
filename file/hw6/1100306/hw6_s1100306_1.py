def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms

    len_nodes = len(nodes)
    

    a = [[float("inf") for _ in range(len_nodes-1)]for _ in range(len_nodes-1)]
    visit = [0 for _ in range(len_nodes)]
    sum = 0
    for j in range(len_nodes - 1):
        for i in range(j, len_nodes-1):
            if i+1 != j:
                a[j][i] = abs(nodes[i+1][0] - nodes[j][0]) + abs(nodes[i+1][1] - nodes[j][1])
        
        if a[j-1][0] == float("inf"):
            a[j-1].pop(0)
            a[j-1].append(float("inf"))
        a[j] = a[j] + [a[j-1][0]]

        visit[j + 1] = min(a[j])
        a[j].remove(min(a[j]))
        
    
    for k in range(len(visit)):
        sum += visit[k]
    return sum

    # len_nodes = len(nodes)
    

    # cost = [float("inf") for _ in range(len_nodes)]
    # cost[0] = 0
    # b = [-1 for _ in range(len_nodes)]
    # visit = [False for _ in range(len_nodes)]
    # sum = 0
    # t = []
    # while len(t) < len_nodes:
    #     mincost = float("inf")
    #     minnode = None
    #     for i in range(len_nodes):
    #         if not visit[i] and cost[i] < mincost:
    #             mincost = cost[i]
    #             minnode = i

    #     t.append(minnode)
    #     visit[minnode] = True
        
    #     for edge in nodes[minnode]:
    #         if not visit[edge[0]] and edge[1] < cost[edge[0]]:
    #             cost[edge[0]] = edge[1]
    #             b[edge[0]] = minnode
    
    # for costs in cost:
    #     sum += costs
    #return sum

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    