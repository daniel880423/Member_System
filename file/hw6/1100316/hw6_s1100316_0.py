def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    l = len(nodes)
    lst = []
    for i in range(l-1):
        for j in range(i+1, l):
            path = abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])
            lst.append([i, j, path])
    lst = sorted(lst, key=lambda x: x[2])
    
    tree = dict()
    for i in range(l):
        tree[i] = i
    def find_node(x):
        if tree[x]!=x:
            tree[x]= find_node(tree[x])    
        return tree[x]
    mst=[]
    l = l-1
    for e in lst:
        n1, n2, _ = e
        if find_node(n1)!= find_node(n2):
            tree[find_node(n2)] = find_node(n1)
            mst.append(e)
            l-=1
            if l ==0:
                break
    ll = len(mst)
    sum =0
    for i in range(ll):
        sum += mst[i][2]
    
    return sum
if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    