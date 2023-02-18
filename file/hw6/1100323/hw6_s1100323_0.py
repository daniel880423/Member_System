def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    ans = 0
    a = nodes[0]
    p = [a]
    nodes.remove(a)
    while(nodes): 
        length = 200 
        for i in nodes: 
            for a in p: 
                if abs(a[0]-i[0])+abs(a[1]-i[1]) < length: 
                    length = abs(a[0]-i[0])+abs(a[1]-i[1]) 
                    mini = i 
        p.append(mini) 
        nodes.remove(mini) 
        ans += length
         
   







    return ans

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    