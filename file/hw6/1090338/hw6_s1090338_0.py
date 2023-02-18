def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    n=len(nodes)
    initial = [[float("inf")]*n for i in range(n)] #列出各點之間之距離
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if i!=j:
                initial[i][j]=abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1]) #nodes之間的距離

    selected=list() #建立一個空矩陣
    for i in range(n):
        selected.append(0)  
        
    c = 0   #邊的數目初始值為0，總共會有V-1個邊
    sum=0
    selected[0] = True
    while (c < n - 1): #如果邊常數目沒有大於V-1就繼續迴圈 
        minimum = 99999  #設最小值
        x = 0
        y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if ((not selected[j]) and initial[i][j]):  
                        # not in selected and there is an edge
                        if minimum > initial[i][j]:
                            minimum = initial[i][j]
                            x = i
                            y = j
        sum+=initial[x][y]
        selected[y] = True
        c += 1
    return sum


if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    