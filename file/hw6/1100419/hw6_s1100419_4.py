def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    sum=0
    a=list()
    v=[0]
    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            #xi=nodes[i][0]
            #yi=nodes[i][1]
            #xj=nodes[j][0]
            #yj=nodes[j][1]
            out=abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
            a.append([out,i, j])
    #將各個節點帶入距離公式內計算距離，a為所有數據[距離，節點1，節點2]


    while True:
        if len(v)==len(nodes):
            break

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

        if next not in v:
            v+=[next]
        sum+=x











    return sum

if __name__ == '__main__':
    nodes = [[-9, 10], [-7, 8], [5, 6], [-3, 4],[-1,2],[0,0],[4,2]]
    print(homework_6(nodes))
    # 22
    