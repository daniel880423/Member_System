def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms                                               #此為Kruskal Algorithms
    every_path = [[float("inf")]*len(nodes) for i in range(len(nodes))]                         #假設每個節點間的距離為無限(inf)
    nodes_with_path =[]                                                                         #將陣列整理為[ 起點 , 終點 , 兩相異節點距離 ]的形式
    k = 1                                                                                       #避開無限(inf)
    for start in range(len(nodes)):                                                             #計算每節點間的距離，此範例有節點0、節點1、節點2、節點3、節點4
        for checkpoint in range(len(nodes)):                                                                        
            path = abs(nodes[start][0] - nodes[checkpoint][0]) + abs(nodes[start][1] - nodes[checkpoint][1])        #助教給的距離公式
            if path == 0:                                                                                           #如果為相同節點
                continue                                                                                            #則避開
            else:                                                                                                   #若不同
                every_path[start][checkpoint] = path                                                                #加入兩相異節點之間的距離(如:節點0與節點1相距8，會將every_path的index[0][1]放8)   

    for i in range(len(nodes)):                                                                 #將陣列整理為[ 起點 , 終點 , 兩相異節點距離 ]的形式
        for j in range(k,len(nodes)):                                                            
            path_nodes = [i,j,every_path[i][j]]                                                  
            nodes_with_path.append(path_nodes)                                                   
        k += 1                                                                                  #避開重複的節點 
                                                                                                 
    nodes_with_path.sort(key = lambda s: s[2])                                                  #將路徑由小到大排列
                                                                                                
    pic = [-1]*(len(nodes_with_path)+1)                                                         
                                                                                                
    def find(pic, node_path):                                                                   
        if pic[node_path]< 0:                                                                   
            return node_path                                                                    
        else:                                                                                   
            temp = find(pic,pic[node_path])                                                     
            pic[node_path] = temp
            return temp

    def union(pic ,start ,checkpoint,path ,edge):                                               #並查集(Union_Find 將2棵不一樣的樹合而為一)
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
    
    