def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    l = len(nodes)
    lst = []
    for i in range(l-1):        #將座標點之間的距離算出來
        for j in range(i+1, l):
            path = abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])    #abs:絕對值
            lst.append([i, j, path])
    lst = sorted(lst, key=lambda x: x[2])   #按照距離由小到大排序
    
    tree = dict()       #建立dic用來記錄哪個點連接到哪一個
    for i in range(l):
        tree[i] = i
    def find_node(x):
        if tree[x]!=x:
            tree[x]= find_node(tree[x])    
        return tree[x]

    sum =0      #尋找最小路徑並加起來
    l = l-1
    for e in lst:
        n1, n2, _ = e
        if find_node(n1)!= find_node(n2):
            tree[find_node(n2)] = find_node(n1)
            sum += _
            l-=1
            if l ==0:
                break
    return sum

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    