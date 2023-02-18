def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    import math

    P=[]
#設定初始化參數 P=[0,1,2,3,4...]
    for i in range(len(nodes)):
        P.append(i)


    edges = []
#算距離並建構節點間的距離
    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            x_distance = abs(nodes[i][0] - nodes[j][0])
            y_distance = abs(nodes[i][1] - nodes[j][1])
            edges.append ( [ i, j,x_distance + y_distance,] )



    

        
    edges = sorted(edges, key=lambda x: x[2])
    def _query(x):
        # 如果P[x] != x，說明x不是樹根
        if P[x] != x:
            P[x] = _query(P[x])
        return P[x]
    
    res = 0
    for u, v, w in edges:# u v為節點 w為距離
        root_u = _query(u)
        root_v = _query(v)
        if root_u != root_v: #判斷回傳值一不一樣
            P[root_v] = root_u #不同樹做合併
            res += w #將距離存起來
    return res



    

if __name__ == '__main__':
    nodes = [[20, 15], [25, -35], [18, -17], [24, -4], [-28, 15], [10, 14], [-11, 23], [0, 0], [30, 0], [0, 30]]
    print(homework_6(nodes))
    # 22
    #[[75, 90], [67, 19], [5, 10], [-26, -75], [-26, -24], [82, 62], [-32, 30], [-23, -63], [62, -80], [71, 24], [80, -45], [44, -15], [-12, -90], [-56, 93], [43, -29], [59, 80], [67, -76], [-12, 100], [-99, -40], [49, -45], [-58, 92], [-52, -19], [69, 82], [-3, -21], [-48, -6], [-37, -53], [35, -21], [-14, 53], [-12, -68], [-33, 38], [14, -77], [-12, -65], [-43, -14], [98, 23], [46, -96], [-100, -64], [70, 45], [-91, 43]]