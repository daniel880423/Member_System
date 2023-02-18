def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    sum=0
    a=list()
    v=[0]
    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            xi=nodes[i][0]
            yi=nodes[i][1]
            xj=nodes[j][0]
            yj=nodes[j][1]
            out=abs(xi-xj) + abs(yi-yj)
            a.append([out,i, j])
    #將各個節點帶入距離公式內計算距離，a為所有數據[距離，節點1，節點2]

    path=list()
    for i in range(len(nodes)):
        b=list()
        for j in range(len(nodes)):
            b.append(float('inf'))
        path.append(b)
    
    for i in range(len(a)):
        path[a[i][2]][a[i][1]]=a[i][0]
        path[a[i][1]][a[i][2]]=a[i][0]

    while True:
        if len(v)==len(nodes):
            break
        # x=list()
        # for i in v:
        #     m=min(path[i])
        #     x.append([m,i])
        # x=sorted(x)
        # y=list()
        x = float("inf")
        next = -1
        for i in range(len(v)):
            for j in range(len(a)):
                start = a[j][1]
                end = a[j][2]
                dis = a[j][0]
                if v[i]==start and end not in v:
                    if x > dis:
                        x = dis
                        next = end
                if v[i]==end and start not in v:
                    if x > dis:
                        x = dis
                        next = start



                    # y.append(dis)


        # for j in range(len(path[x[0][1]])):
        #     if path[x[0][1]][j]==x[0][0] and j not in v:
        # path[x[0][1]][j]==float('inf')
        # path[j][x[0][1]]==float('inf')
        if next not in v:
            v+=[next]
        sum+=x











    return sum

if __name__ == '__main__':
    nodes = [[-1, 18], [11, 19], [-13, -18], [-17, 0]]
    print(homework_6(nodes))
    # 22
    