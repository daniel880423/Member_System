def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    num_node=len(nodes)         ##計算有幾個節點
    nearest=[]                  ##創建最近節點矩陣
    distance=[]                 ##創建最近距離矩陣
    path=[]                     ##創建特徵矩陣
    num=0                       ##設立變數，初值設為0

    for i in range(num_node):               ##利用曼哈頓公式計算各節點間的距離，並放入特徵矩陣
        path.append([])
        for j in range(num_node):
            if  i==j:
                path[i].append(float("inf"))      ##主對角線皆設為無限大
            else :
                path[i].append(abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1]))  
        if i!=0:
            nearest.append(0)                ##最近節點矩陣設為0
            distance.append(path[0][i])      ##複製特徵矩陣



    for i in range(num_node):  
        min_num=float("inf")
        for j in range(num_node-1):                        ##找出distance中最小的數值，並放入min_num
            if (0<=distance[j] and distance[j]<min_num):   ##紀錄當前節點放入 vnear
                min_num=distance[j]
                vnear=j+1


        if min_num!=float("inf"):                           ##如果上面有找到最小數值，進入

            num+=min_num                                    ##將數值加進num裡

            distance[vnear-1]=-1                            ##distance位址設為-1
            for k in range(num_node):                       ##更新最近節點矩陣與最近距離矩陣
                if (path[k][vnear]<distance[k-1]):

                    distance[k-1]=path[k][vnear]

                    nearest[k-1]=vnear

    return num

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    