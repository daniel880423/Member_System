def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    sum = 0
    a = list()
    b = [0]

    #算所有點之間的距離
    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            xi = nodes[i][0]
            yi = nodes[i][1]
            xj = nodes[j][0]
            yj = nodes[j][1]
            distance = abs(xi-xj) + abs(yi-yj)
            a.append([distance,i, j])

    #設一個矩陣為無限大
    path = list()
    for i in range(len(nodes)):
        c = list()
        for j in range(len(nodes)):
            c.append(float('inf'))
        path.append(c)
    
    #距離填滿矩陣
    for i in range(len(a)):
        path[a[i][2]][a[i][1]] = a[i][0]
        path[a[i][1]][a[i][2]] = a[i][0]

    #把算最短路徑設為無限大，使下次不會重複加到
    while True:
        if len(b) == len(nodes):
            break

        x = float("inf")
        next = -1
        for i in range(len(b)):
            for j in range(len(a)):
                start = a[j][1]
                end = a[j][2]
                dis = a[j][0]
                if b[i] == start and end not in b :
                    if x > dis:
                        x = dis
                        next = end

        b += [next]
        sum += x


    return sum

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    