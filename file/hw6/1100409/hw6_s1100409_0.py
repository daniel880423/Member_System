def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    AAA = 0
    Th = nodes[0]
    ze = [Th]
    nodes.remove(Th)
    while(nodes): 
        cm = 200 
        for y in nodes: 
            for Th in ze: 
                if abs(Th[0]-y[0])+abs(Th[1]-y[1]) < cm: 
                    cm = abs(Th[0]-y[0])+abs(Th[1]-y[1]) 
                    zen = y 
        ze.append(zen) 
        nodes.remove(zen) 
        AAA+=cm
    return AAA

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
