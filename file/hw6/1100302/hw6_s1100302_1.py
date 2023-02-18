def homework_6(nodes):
    total = 0                                                       #建立變數儲存答案                    
    start = nodes[0]                                                #選取node的第一個點作為起點
    Y = [start]                                                     #建立一個list存放已連線節點
    nodes.remove(start)                                             #把已連線的節點從所有節點中刪除
    while(nodes):                                                   #當nodes不為空list代表還有節點尚未被連接
        length = float("inf")                                       #先將length預設值設為無限大
        for p1 in nodes:                                            #在未連接過的節點中選出一個節點進行比較
            for p2 in Y:                                            #在已連接過的節點中選出一個節點進行比較
                if abs(p2[0]-p1[0])+abs(p2[1]-p1[1]) < length:      #如果新距離比原距離短
                    length = abs(p2[0]-p1[0])+abs(p2[1]-p1[1])      #用新距離取代原距離
                    minpoint = p1                                   #找出最短距離節點
        Y.append(minpoint)                                          #將最短距離節點放入Y   
        nodes.remove(minpoint)                                      #將已連接的節點移出nodes
        total+=length                                               #把距離加上答案
    return total

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
