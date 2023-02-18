def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms


    node_num=len(nodes)

    v=[[float("inf") for j in range(node_num)] for i in range(0,node_num)]  #設一個矩陣

    for i in range(node_num):   #每個點(i)到其他點(j)的距離(有包括自己到自己)存入矩陣
        nodei_x=nodes[i][0]      #橫軸座標
        nodei_y=nodes[i][1]      #垂直軸座標
        for j in range(node_num):
            nodej_x=nodes[j][0]     #橫軸座標
            nodej_y=nodes[j][1]     #垂直軸座標
            if i!=j:      #如果是原本的點到原本的點的話，將它對應到矩陣的點設為inf(原本距離為0的，剛好是對角線)
                v[i][j]=abs(nodei_x-nodej_x)+abs(nodei_y-nodej_y)


    """
    [[inf, 8, 12, 10, 8], 
     [8, inf, 4, 6, 10], 
     [12, 4, inf, 8, 12], 
     [10, 6, 8, inf, 4], 
     [8, 10, 12, 4, inf]]"""

    """
    [[inf, 7, 8, 7], 
    [7, inf, 3, 8], 
    [8, 3, inf, 7], 
    [7, 8, 7, inf]]"""


    visit=[]  #設一個list存經過的節點(ex:0.[3,1],    1.[2,7],    2.[4,8],    3.[7,4]])
    
    sum=0 #存經過的距離

    visit.append(0)  #先把起始點設為0.(也就是[3,1])

    while(len(visit)!=len(nodes)):   #在visit經過的節點數不等於輸入的nodes數的情況下一直跑迴圈
        x=[]   #先設一個list，分別存各點(row起點)到其他點(col終點)的[row(起點),col(終點),lon(長度)]
        for i in visit:  #在經過的節點中
            m=min(v[i])  #有經過的節點(row起點)到其他點(col終點)的最小值
            idx=v[i].index(m)  #設一變數存最小值在節點(row起點)到其他點(col終點)(也就是v的橫軸中)的位置(縱軸)[也就是終點]
            x.append([i,idx,m])  #依照[row(起點節點),col(最小值在v的橫軸的位置(縱軸)[終點])),lon(長度)]這個模式存入x
        x = sorted(x, key=lambda y:y[2])  #把x內存入的所有list([row(起點),col(最小值在v的橫軸的位置(縱軸)[終點節點]),lon(長度)])，依長度(x內的各個小list的第三個)排序---->第一個(x[0])一定是最短的

        row = x[0][0]      #用row存最短距離的起點節點(橫軸)
        col=x[0][1]        #用col存最小值(m)在v的橫軸的位置[起點到終點的終點節點](縱軸)
        lon=x[0][2]        #用lon存最短距離
        if col in visit:      #如果最小值在v的橫軸的位置已經在visit(經過的節點)內
            v[row][col]=float("inf")    #就把v中的那個點設成無限大
            v[col][row]=float("inf")    #以inf為對角線對稱的值也要設成無限大
        else:                 #如果最小值在v的橫軸的位置在沒visit(經過的節點)內
            visit.append(col)  #把最小值在v的橫軸的位置存入visit(經過的節點)
            v[row][col]=float("inf")   #存入visit後，在把v中的那個點設成無限大
            v[col][row]=float("inf")   #以inf為對角線對稱的值也要設成無限大
            sum+=lon          #把距離加進sum

            

    return sum  #回傳

if __name__ == '__main__':
    nodes =  [[3,1],[2,7],[4,8],[7,4]] #17    
    #nodes =  [[0,0],[2,6],[3,9],[6,4],[7,1]]# 22
    print(homework_6(nodes))

    """error
    nearest=[]
    distance=[]  
    for i in range(node_num):
        nearest.append(0)
        distance.append(0)
    for i in range(node_num):
        nearest[i]=1
        distance[i]=v[0][i]

    visit=0
    sum=0 
    time=0    
    while(time<=node_num):

        min=float("inf")
        for i in range(node_num):
            if (0<=distance[i]<min):
                min=distance[i]
                visit=i

        distance[visit]=-1
        for i in range(node_num):
            if (v[i][visit]<distance[i]):
                distance[i]=v[i][visit]
                nearest[i]=visit
                sum+=distance[i]

        time+=1

"""