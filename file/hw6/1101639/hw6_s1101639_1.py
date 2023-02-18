def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    ans = 0
    x = nodes[0]
    v = [x]
    nodes.remove(x)
    while(nodes): 
        length = 200 
        for y in nodes: 
            for x in v:  
                if abs(x[0]-y[0])+abs(x[1]-y[1]) < length: 
                    length = abs(x[0]-y[0])+abs(x[1]-y[1]) 
                    miny = y 
        v.append(miny)    
        nodes.remove(miny) 
        ans+=length
    return ans

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
   
    