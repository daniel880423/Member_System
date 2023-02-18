def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    all_path = [[float("inf")]*len(nodes) for i in range(len(nodes))]                      #假設每點間的距離為無限
    nodes_path =[]
    k = 1
    for i in range(len(nodes)):                                                            #計算每點間的距離
        for ck in range(len(nodes)):
            path = abs(nodes[i][0] - nodes[ck][0]) + abs(nodes[i][1] - nodes[ck][1])       
            if path == 0:
                continue
            else:
                all_path[i][ck] = path                                                     #path放進all_path                                                            

    for i in range(len(nodes)):                                                            #將陣列整理為[起點 , 終點, 距離的形式]
        for j in range(k,len(nodes)):
            path_nodes = [i,j,all_path[i][j]]
            nodes_path.append(path_nodes)
        k += 1

    nodes_path.sort(key = lambda s: s[2])                                                  #將路徑以小到大排列
    
    pic = [-1]*(len(nodes_path)+1)

    def find(pic, node_path):                                                              #遞迴尋找所屬集合的父節點
        if pic[node_path]< 0:
            return node_path
        else:
            temp = find(pic,pic[node_path])
            pic[node_path] = temp
            return temp

    def union(pic ,start ,checkpoint,path ,edge):                                          #合併
        temp_start = start
        temp_checkpoint = checkpoint
        start = find(pic,start)
        checkpoint = find(pic,checkpoint)
        if start != checkpoint:
            edge.append([temp_start,temp_checkpoint,path])
            if pic[start] < pic[checkpoint]:
                pic[start] = pic[start]+pic[checkpoint]
                pic[checkpoint] = start
            else:
                pic[checkpoint] = pic[start]+pic[checkpoint]
                pic[start] = checkpoint

    edge = []
    total_path = 0

    for start,checkpoint,path in nodes_path:
        union(pic, start , checkpoint ,path ,edge)
    for ans in edge:
        total_path += ans[2]

    return total_path



if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    