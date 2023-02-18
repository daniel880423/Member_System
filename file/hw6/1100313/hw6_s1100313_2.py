def homework_6(nodes):                                                       #prim演算法
    F=[]                                                                     #存放節點的地方
    total=0                                                                  #初始總合為0
    F.append(nodes[0])                                                       #假設初始節點
    while len(F)!= len(nodes):                                               #當傑點沒有全部找齊，持續迴圈
        shortest=float("inf")                                                #初始最短距離為無限
        for i in F:
            for j in range(0, len(nodes)):
                if nodes[j] in F:                                            #若節點已經在F裡，則直接換下一個node
                    continue
                else:                                                        #若節點不在F裡
                    distance=abs(i[0]-nodes[j][0])+abs(i[1]-nodes[j][1])     #計算目前的node和F裡的節點之間的距離
                    if distance<shortest:                                    #如果距離比目前最短的距離短
                        shortest=distance                                    #取代它
                        point=nodes[j]                                       #紀錄是哪個節點的距離和F裡面的節點最短
        F.append(point)                                                      #每算完一輪，把剛剛記錄下來的節點加進F裡
        total+=shortest                                                      #計算總距離
    return total

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    