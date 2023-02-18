def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    total=0
    a=list()
    vis=[0]
    #算出所有點之間的距離
    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            xi = nodes[i][0]
            yi = nodes[i][1]
            xj = nodes[j][0]
            yj = nodes[j][1]
            #距離公式|xi-xj| + |yi-yj|
            out = abs(xi-xj) + abs(yi-yj)
            a.append([out,i, j]) 


    #當vis裡面的節點數<所有節點數時執行
    while len(vis) < len(nodes):
        x = float("inf")
        for i in range(len(vis)):
            for j in a:
                start = j[1]     #start為目前走道的節點數
                end = j[2]       #end為已走過的
                dis = j[0]
                if vis[i] == start and end not in vis :
                    if x > dis:
                        x = dis
                        next = end
                if vis[i] == end and start not in vis :
                    if x > dis:
                        x = dis
                        next = start

        vis += [next]
        total += x


    return total

if __name__ == '__main__':
    nodes = [[-1,18],[11,19],[-13,-18],[-17,0]]
    print(homework_6(nodes))
    # 22

    