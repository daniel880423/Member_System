def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal 
    ln = len(nodes)
    A = []
#計算各點距離
    for i in range(ln-1):
        for j in range(i+1,ln):
            distance = 0
            for k in range(2):
                distance += abs(nodes[i][k]-nodes[j][k])
            A.append([distance,i,j])
#算好後距離由小到大排列
    A.sort()

    trees = dict()
    for i in range(ln):
        trees[i] = i
#尋找根節點
    def find(x):
        if trees[x] != x:
            trees[x] = find(trees[x])
        return trees[x]
#定義最小生成樹
    p = []
    ln -= 1
#跑一個循環
    for e in A:
        _, n1, n2 = e
        if find(n1) != find(n2):
          trees[find(n2)] = find(n1)
          p.append(e)
          ln -= 1
          if ln == 0:
                break
    f = len(p)
    sum = 0
#距離相加
    for i in range(f):
        sum += p[i][0]

    return sum

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    