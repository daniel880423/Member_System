def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    n=len(nodes)
    initial = [[float("inf")]*n for i in range(n)] #列出各點之間之距離
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if i!=j:
                initial[i][j]=abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1]) #nodes之間的距離

    selected=list() #建立一個空list存已經過的點
    for i in range(n):
        selected.append(0)  
        
    edge=0   #邊的數目
    sum=0    #最小距離之總
    selected[0]=True

    while(edge < n-1):  #如果邊沒有大於n-1就繼續迴圈 
        minimum = 99999 #最短距離
        start = 0   #起點
        next = 0    #下個點
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if ((not selected[j]) and initial[i][j]):   #沒有被經過的點且有距離可使用
                        if minimum > initial[i][j]:             #i到j最短距離
                            minimum = initial[i][j]
                            start = i
                            next = j
        sum+=initial[start][next]
        selected[next] = True
        edge += 1 #邊＋１
    return sum


if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    