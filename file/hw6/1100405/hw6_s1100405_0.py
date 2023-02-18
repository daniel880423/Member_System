def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    global sum
    sum = 0
    visit = [nodes[0]]
    
    def Prim(V, N):
        global sum
        distance = float('inf')

        for i in V:
            for j in N:
                if j not in V:
                    D = abs(i[0]-j[0])+abs(i[1]-j[1])
                    if distance > D:
                        distance = D
                        Vlist = j
        sum += distance
        V.append(Vlist)

        if len(V) == len(N):
            return sum
        else:    
            return Prim(V, N)
                    
    Prim(visit, nodes)
    return sum

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    