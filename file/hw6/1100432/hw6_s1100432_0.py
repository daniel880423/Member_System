def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    a = 0
    y = nodes[0]
    vector = [y]
    nodes.remove(y)
    while(nodes): 
        long = 200 
        for y in nodes: 
            for y in vector: 
                if abs(y[0]-y[0])+abs(y[1]-y[1]) < long: 
                    long = abs(y[0]-y[0])+abs(y[1]-y[1]) 
                    zi = y 
        vector.append(zi) 
        nodes.remove(zi) 
        a+=long
    return a

if __name__ == '__main__':
    nodes = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(homework_6(nodes))
    