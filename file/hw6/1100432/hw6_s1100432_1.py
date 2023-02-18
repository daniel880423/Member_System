def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    answer = 0
    x1 = nodes[0]
    vector = [x1]
    nodes.remove(x1)
    while(nodes): 
        long = 200 
        for y in nodes: 
            for x1 in vector: 
                if abs(x1[0]-y[0])+abs(x1[1]-y[1]) < long: 
                    long = abs(x1[0]-y[0])+abs(x1[1]-y[1]) 
                    miny1 = y 
        vector.append(miny1) 
        nodes.remove(miny1) 
        answer+=long
    return answer

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
   
    