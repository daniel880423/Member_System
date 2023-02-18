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
            #距離公式|xi-xj| + |yi-yj|
            out=abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
            a.append([out,i, j]) 
            a.append([out,j, i])
    #將各個節點帶入距離公式內計算距離，a為所有數據[距離，節點1，節點2]

    while len(v)<len(nodes):
    #當v裡面的節點數<所有節點數時執行
        x = float("inf")
        next = -1
    
        for i in range(len(v)):
            for j in a:
                start = j[1]
                end = j[2]
                dis = j[0]
                if v[i]==start and end not in v and x > dis:
                    x = dis
                    next = end
                if v[i]==end and start not in v and x > dis:
                    x = dis
                    next = start
        #找出最短路徑，並且記錄中繼點

        v+=[next]
        sum+=x


    return sum

if __name__ == '__main__':
    nodes = [[-1,18],[11,19],[-13,-18],[-17,0]]
    print(homework_6(nodes))
    # 22
    