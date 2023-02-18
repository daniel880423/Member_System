def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    S=0
    all=list()
    U=[0]
    #計算各節點之間的距離
    for i in range(len(nodes)-1):
        for j in range(i+1,len(nodes)):
            out=abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
            #out=|xi-xj| + |yi-yj|
            all.append([out,i,j])        
            #all=[out,i,j]=[距離,節點1,節點2]
    
    
    #比較出最短路徑並找出中繼點    
    while len(U)<len(nodes):    #當U裡的節點數 < 所有節點數時
        x = float("inf")
        for i in range(len(U)):
            for j in all:
                start = j[1]
                end = j[2]
                dis = j[0]
                if U[i]==start and end not in U :
                    if x > dis:
                        x = dis
                        next = end
                if U[i]==end and start not in U :
                    if x > dis:
                        x = dis
                        next = start
        
        
        U+=[next]
        S+=x

    return S

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    