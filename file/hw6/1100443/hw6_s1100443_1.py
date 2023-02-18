def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    sum=0
    A=list()
    v=[0]
    for i in range(len(nodes)-1):
        for j in range(i+1,len(nodes)):
            #xi=nodes[i][0]
            #yi=nodes[i][1]
            #xj=nodes[j][0]
            #yj=nodes[j][1]
            out=abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])
            A.append([out,i,j]) 


    while len(v)<len(nodes):
    #當v裡面的節點數<所有節點數時執行
        x = float("inf")
        for i in range(len(v)):
            for j in A:
                start = j[1]
                end = j[2]
                d = j[0]
                if v[i]==start and end not in v :
                    if x > d:
                        x = d
                        next = end
                if v[i]==end and start not in v :
                    if x > d:
                        x = d
                        next = start
        #找出最短路徑，記錄中繼點

        v += [next]
        sum += x


    return sum



if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    