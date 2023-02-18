def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    every_path = [[float("inf")]*len(nodes) for i in range(len(nodes))]                        #假設每點間的距離為無限
    nodes_with_path =[]
    k = 1
    for start in range(len(nodes)):                                                            #計算每點間的距離
        for checkpoint in range(len(nodes)):
            path = abs(nodes[start][0] - nodes[checkpoint][0]) + abs(nodes[start][1] - nodes[checkpoint][1]) 
            if path == 0:
                continue
            else:
                every_path[start][checkpoint] = path                                                               

    for i in range(len(nodes)):                                                                #將陣列整理為[起點 , 終點, 距離的形式]
        for j in range(k,len(nodes)):
            path_nodes = [i,j,every_path[i][j]]
            nodes_with_path.append(path_nodes)
        k += 1

    nodes_with_path.sort(key = lambda s: s[2])                                                 #將路徑以小到大排列
    
    pic = [-1]*(len(nodes_with_path)+1)

    def find(pic, node_path):
        if pic[node_path]< 0:
            return node_path
        else:
            temp = find(pic,pic[node_path])
            pic[node_path] = temp
            return temp

    def union(pic ,start ,checkpoint,path ,edge):
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

    for start,checkpoint,path in nodes_with_path:
        union(pic, start , checkpoint ,path ,edge)
    for ans in edge:
        total_path += ans[2]

    return total_path

if __name__ == '__main__':
    nodes =[[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    






  