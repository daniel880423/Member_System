def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    vertic=len(nodes)                                            #使用Kruskal Algorithms
    lst=[]
    for i in range(vertic-1):                                    #算出每一點到每一點的距離
        for j in range (i+1,vertic):
            x=abs((nodes[i][0]-nodes[j][0]))
            y=abs((nodes[i][1]-nodes[j][1]))
            distance=x+y
            lst.append([distance,i,j])
            lst.sort()                                           #進行由小排到大

    ori_trees = dict()                                           #每個頂點視為一棵節點樹，可以用字典表示，鍵表示頂點，鍵值表示頂點所在樹的節點
    for i in range(vertic):                                      
        ori_trees[i] = i
    def find_node(x):                                            #尋找根節點
        if ori_trees[x]!=x:
            ori_trees[x]= find_node(ori_trees[x])    
        return ori_trees[x]

    p=[]                                                         #定義最小生成樹
    vertic = vertic-1
    for e in lst:                                                #進行循環
        _ ,n1, n2= e
        if find_node(n1)!= find_node(n2):
            ori_trees[find_node(n2)] = find_node(n1)
            p.append(e)
            vertic-=1
            if vertic ==0:
                break
    f = len(p)
    sum =0
    for i in range(f):                                           #把最短距離相加
        sum += p[i][0]
    
    return sum





if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    