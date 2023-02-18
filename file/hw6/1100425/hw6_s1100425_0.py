def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    global w
    w = [i for i in range(0, 105)]
    edges = []
    for i, ix in enumerate(nodes):          #i,ix 為nodes的編號及內容
        for j, jx in enumerate(nodes):      #j,jx 為nodes的編號及內容
            if j > i:
                edges.append((i, j, abs(ix[0] - jx[0]) + abs(ix[1] - jx[1])))

    edges.sort(key=lambda x: x[2])
    
    count = 0
    j = 0
    for i in edges:   
        if find_root(i[0]) != find_root(i[1]) and j <= 105:
            count += i[2]
            union(i[0], i[1])
            j += 1
    w = []
    return count

def find_root(x): #查找集合
    if x != w[x]:
        w[x] = find_root(w[x])
    return w[x]

def union(x, y): #合併集合
    x_root, y_root = find_root(x), find_root(y)
    if x_root != y_root:
        w[x_root] = y_root

    return 

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    