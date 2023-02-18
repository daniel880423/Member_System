def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    ans = 0
    x = nodes[0]
    v = [x]
    nodes.remove(x)
    while(nodes): #當nodes節點未全部連接
        length = 200 #-100 <= xi,yi <= 100 所以length最大值為200
        for y in nodes: #在未連接過的節點中選出
            for x in v: #在已連接過的節點中選出一個x與y連接 
                if abs(x[0]-y[0])+abs(x[1]-y[1]) < length: #如果x到y的距離比length短
                    length = abs(x[0]-y[0])+abs(x[1]-y[1]) 
                    miny = y #當前離已連接節點最短距離的y
        v.append(miny) #將要連接的y放入v   
        nodes.remove(miny) #將已連接的y移出nodes
        ans+=length
    return ans

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    