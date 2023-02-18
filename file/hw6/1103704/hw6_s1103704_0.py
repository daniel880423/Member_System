def distance(nodes):
    path = []
    for i in range(0,len(nodes)):
        for j in range(1,len(nodes)):
            if i!=j and i<j:
                d = abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])
                path.append([d,i,j])
    return path
def find(x,p):
    if p[x]!=x:
        p[x] = find(p[x],p)
    return p[x]

def homework_6(nodes): 
    gggg = 0
    Ans = []
    p =[]
    for i in range(len(nodes)):
        p.append(i)
    a = distance(nodes)
    a.sort()
    for i in range(0,len(a)):
        if len(Ans) == len(nodes)-1:
            break
        if find(a[i][1],p)!= find(a[i][2],p):
            Ans.append((a[i][1],a[i][2]))
            p[find(a[i][1],p)] = find(a[i][2],p)
            gggg+= a[i][0]
    return gggg







    

if __name__ == '__main__':
    nodes = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(homework_6(nodes))
   
    