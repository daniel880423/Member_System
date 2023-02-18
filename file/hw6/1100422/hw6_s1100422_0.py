def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    total=0
    A=list()
    passed=[0]
    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            #xi=nodes[i][0],yi=nodes[i][1],xj=nodes[j][0],yj=nodes[j][1]
            #距離公式|xi-xj| + |yi-yj|將各點帶入
            dis_2=abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
            A.append([dis_2,i, j]) 
    #將所有節點帶入距離公式內，並計算出距離放入A矩陣，A矩陣為所有數據[距離，起始點，結束點]

    while len(passed)<len(nodes):
    #passed用來紀錄經過的節點
    #當passed裡面的節點數<所有節點數時執行
        n = float("inf")
        for i in range(len(passed)):
            for j in A:
                start = j[1]
                end = j[2]
                dis = j[0]
                if passed[i]==start and end not in passed :
                #確定是不是最短路徑且可不可以放進v裡
                    if n > dis:
                        n = dis
                        next = end
                if passed[i]==end and start not in passed :
                #確定是不是最短路徑且可不可以放進v裡
                    if n > dis:
                        n = dis
                        next = start
        #找出最短路徑，並且記錄中繼點

        passed+=[next]
        total+=n


    return total 

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    