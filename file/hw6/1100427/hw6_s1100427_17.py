def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    sumlst = []
    total = 0
    l = len(nodes) - 1
    for i in range(l):
        for j in range(l-i):
            d = abs(nodes[i][0] - nodes[j+1+i][0]) + abs(nodes[i][1] - nodes[j+1+i][1])  # 計算各點之間距離
            lst = []   # 建立一個新list
            lst.append(d)
            lst.append(i)
            lst.append(j+1+i)
            sumlst.append(lst)   # 將list合併
    sumlst = sorted(sumlst)    # 排序
    p = []
    for idx in range(l+1):   # 使用 Kruskal Algorithms
        p.append(idx)
    
    def find(idx):   # 建立find函式
        if p[idx] == idx:
            return idx
        else:
            return find(p[idx])

    for idx in range(len(sumlst)):
        if find(sumlst[idx][1]) != find(sumlst[idx][2]):
            p[find(sumlst[idx][1])] = find(sumlst[idx][2])
            
            total += sumlst[idx][0]

    return total

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    