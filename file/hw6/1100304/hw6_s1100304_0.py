def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    lst = []
    for n1 in range(len(nodes)-1):  #各點距離
        for n2 in range(n1+1,len(nodes)):
            disx = (nodes[n1][0] - nodes[n2][0])**2
            disy = (nodes[n1][1] - nodes[n2][1])**2
            edge = disx**(0.5) + disy**(0.5)
            lst.append([n1,n2,int(edge)])

    lst.sort(key=lambda x:x[2])  #依距離 短-->長 排序

    parent = []
    for node in range(len(nodes)):
        parent.append(node)
        
    i, num_edge = 0, 0
    result = []
    while num_edge < len(nodes) - 1:
        u, v, w = lst[i]
        p = find_root(parent, u)
        q = find_root(parent, v)
        i += 1
        if p != q:
            num_edge += 1
            result.append([u, v, w])
            connect(parent, p, q)
            
    weight = 0  
    for w in range (len(result)):  #路徑相加
        weight += result[w][2]
    
    return weight


def find_root(root, i):  #找含有i的子樹的根節點
    if root[i] == i:
        return i
    return find_root(root, root[i])

def connect(root, x, y):  #連接包含 x & y　的子樹
    xroot = find_root(root, x)
    yroot = find_root(root, y)
    if xroot < yroot:
        root[xroot] = yroot
    elif xroot > yroot:
        root[yroot] = xroot
    else:
        root[yroot] = xroot
        xroot += 1     

if __name__ == '__main__':
    nodes = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(homework_6(nodes))
    # 20
    