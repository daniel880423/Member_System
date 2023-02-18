def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    ans = 0
    x = nodes[0]
    v = [x]
    nodes.remove(x)
    while(nodes): #當nodes節點未連接完成
        length = 200 #length最大值為200
        for y in nodes: #從未連接過的節點中選出
            for x in v: #在已連接過的節點中選出一個x與y連接 
                if abs(x[0]-y[0])+abs(x[1]-y[1]) < length: #如果x到y的距離比length還短
                    length = abs(x[0]-y[0])+abs(x[1]-y[1]) #把length的值改為x到y距離
                    minl = y #距離已連接節點最短距離的y
        v.append(minl) #將要連接的y放入v   
        nodes.remove(minl) #將已連接的y移出nodes
        ans+=length
    return ans

if __name__ == '__main__':
    nodes = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(homework_6(nodes))