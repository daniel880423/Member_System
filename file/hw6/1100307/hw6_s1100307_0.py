def find(x,p):
    if p[x]!=x:
        p[x] = find(p[x],p)
    return p[x]
def distance(nodes):
    path = []
    for i in range(0,len(nodes)):
        for j in range(1,len(nodes)):
            if i!=j and i<j:
                c = abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])
                path.append([c,i,j])
    return path
def homework_6(nodes): 
    anss = 0
    ans = []
    p =[]
    for i in range(len(nodes)):
        p.append(i)
    a = distance(nodes)
    a.sort()
    for i in range(0,len(a)):
        if len(ans) == len(nodes)-1:
            break
        if find(a[i][1],p)!= find(a[i][2],p):
            ans.append((a[i][1],a[i][2]))
            p[find(a[i][1],p)] = find(a[i][2],p)
            anss+= a[i][0]
    return anss









    

if __name__ == '__main__':
    nodes = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(homework_6(nodes))
    # 22
    