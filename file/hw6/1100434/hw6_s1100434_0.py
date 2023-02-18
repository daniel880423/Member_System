def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    count = 0
    i = nodes[0]
    p = [i]
    nodes.remove(i)
    while(nodes):                                                #當nodes節點未全部連接
        length = 200                                             #-100 <= xi,yi <= 100 所以length最大值為200
        for j in nodes:                                          #在未連接過的節點中選出
            for i in p:                                          #在已連接過的節點中選出一個x與y連接 
                if abs(i[0]-j[0])+abs(i[1]-j[1]) < length:       #如果x到y的距離比length短
                    length = abs(i[0]-j[0])+abs(i[1]-j[1]) 
                    minj = j                                     #當前離已連接節點最短距離的y
        p.append(minj)                                           #將要連接的y放入v   
        nodes.remove(minj)                                       #將已連接的y移出nodes
        count += length
    return count

if __name__ == '__main__':
    nodes = [[3,1],[2,7],[4,8],[7,4]]
    print(homework_6(nodes))
    # 17