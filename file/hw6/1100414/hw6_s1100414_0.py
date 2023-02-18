def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    visit=[nodes[0]] #設定visit初始節點
    global sum
    sum=0
    def prim(visiting,Nodes): #定義Prim的函式
        global sum
        distance=100
        for i in visiting:
            for j in Nodes:
                if j not in visiting:
                    x=i[0]-j[0] #計算兩座標(xi,yi),(xj,yj)間的距離
                    y=i[1]-j[1]
                    if distance>(abs(x)+abs(y)):
                        distance=(abs(x)+abs(y)) #取出最短距離
                        addvisiting=j 
        sum=sum+distance
        visiting.append(addvisiting) #把節點加入
        if len(visiting)==len(Nodes): #如果visit長度等於節點總數數，返回最小生成樹的最短距離
            return sum
        else: #否則繼續尋找
            return prim(visiting,Nodes)

    prim(visit,nodes)

    return sum

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    