def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms

    len_nodes = len(nodes)
    nearest = [0 for _ in range(len_nodes-1)]
    distance = [0 for _ in range(len_nodes-1)]
    vnear = 0
    sum = 0
    F = []
    W = [[0 for _ in range(len_nodes)] for _ in range(len_nodes)]
    for i in range(len_nodes):
        for j in range(len_nodes):
            W[i][j] = float("inf")
            if i == j:
                W[i][j] = 0
    for j in range(len_nodes):
        for i in range(len_nodes):
            if i != j:
                W[j][i] = abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1])


    for k in range(len_nodes-1):
        distance[k] = W[0][k+1]

    for i in range(len_nodes-1):
        min = float("inf")
        for j in range(len_nodes-1):
            if(0 <= distance[j] < min):
                min = distance[j]
                vnear = j

        F.append(min)
        distance[vnear] = -1
        for i in range(len_nodes-1):
            if (W[i+1][vnear+1] < distance[i]):
                distance[i] = W[i+1][vnear+1]
                nearest[i] = vnear

    for k in range(len(F)):
        sum += F[k]
    return sum

if __name__ == '__main__':
    nodes = [[-9, 10], [-7, 8], [5, 6], [-3, 4], [-1, 2], [0, 0], [4, 2]]
    print(homework_6(nodes))
    # 22
    