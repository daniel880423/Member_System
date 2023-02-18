def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms

    dis = 0     #先設距離為0   
    z=nodes[0] 
    nodes.remove(z)
    new=[z]       #新節點排序
    #print(new)
    #print(nodes)
    #print()

    while(nodes):
        l=201       #最大距離
        for y in new: 
            for x in nodes:
                if x==y :       #判斷座標是否重複
                    nodes.remove(x)
                else:
                    if abs(x[0]-y[0])+abs(x[1]-y[1]) < l:      #絕對值距離不超過201
                        l=abs(x[0]-y[0])+abs(x[1]-y[1])
                        min=x       #找出最小距離的節點
        new.append(min)      #新:加入最短節點
        nodes.remove(min)       #移出最短節點
        dis+=l
        #print(new)
        #print(nodes)
        #print()

    return dis

if __name__ == '__main__':
    nodes = [[3,1],[2,7],[4,8],[7,4]]
    print(homework_6(nodes))
    # 22

