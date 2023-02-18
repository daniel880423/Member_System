def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    l = len(nodes)
    #建立節點間距離矩陣
    m=[]
    for i in range(l):
        for j in range(i+1,l):
            distance = abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])
            m.append([i,j,distance])
            m.append([j,i,distance])
    m.sort(key = lambda x:x[0])
    visit=[0]#走訪節點
    edge=[]#邊
    ans = 0
    #走訪節點小於總結點數表示未完成
    while len(visit)<l:
        for i in m:
            if i[0]==visit[-1]:
                edge.append(i)
        # for i in range(visit[-1]*(l-1),(visit[-1]+1)*(l-1)):
        #     edge.append(m[i])
        #依長度由大至小排列
        edge.sort(key = lambda x:x[2],reverse=True)
        #將最短距離加入ans，並此節點加入visit        
        while (1):
            if edge[-1][1] not in visit:
                visit.append(edge[-1][1])
                ans+=edge[-1][-1]             
                break
            else:
                edge.pop()
            


    return ans










if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    