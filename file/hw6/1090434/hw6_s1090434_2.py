def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal
    global sum
    sum=0
    V=[nodes[0]]
    def P(V, nodes):
        global sum
        d=101
        for i in V:
            for j in nodes:
                if j not in V:
                    if d>abs(i[0]-j[0])+abs(i[1]-j[1]):
                        d=abs(i[0]-j[0])+abs(i[1]-j[1])
                        VV=j
        sum+=d
        V.append(VV)
        if len(V)==len(nodes):
             return sum
        else:
             return P(V, nodes)
    P(V, nodes)                
    return sum

if __name__ == '__main__':
    nodes = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(homework_6(nodes))
    # 22
    