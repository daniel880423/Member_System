def homework_6(nodes): 
    i=j=1
    lenth=len(nodes)
    V = [[float("inf")for j in range(lenth)]for k in range(lenth)] #建立一個list V用來表示點到點的距離
    d=list() #建立一個list d 用來放各節點的距離、起點、終點
    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            out=abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
            d.append([out,i, j])
            d.append([out,j,i])
    for i in range(len(d)): #把距離依序填入，形成完整的list V
        V[d[i][2]][d[i][1]]=d[i][0]
        V[d[i][1]][d[i][2]]=d[i][0]
    visit=[0] #list visit表示拜訪過的節點，一開始的初始節點自行設定，這邊設定為V0
    s = 0
    while True:
        if len(visit)==lenth: #若visit長度等於節點長度表示所有節點都已走訪過，終止迴圈
            break
        x = float("inf") #x為用來比較距離大小的初始參數，由於需求出最小距離，故先設為無限大
        next = -1 #用來存取拜訪過的節點
        for i in range(len(visit)):
            # for j in range(len(d)):
            #     start = d[j][1]
            #     end = d[j][2]
            #     dis = d[j][0]
            for j in d:
                start=j[1]
                end=j[2]
                dis=j[0]
                if visit[i]==start and end not in visit : #需注意1.當前start值需等於目前走訪之節點 2.end值不能是已走訪的節點
                    if x > dis:
                        x = dis
                        next = end
        visit+=[next] #加上走訪過的節點
        s +=x #加上最小距離
    return s

if __name__ == '__main__':
    nodes = [[-1,18],[11,19],[-13,-18],[-17,0]]
    print(homework_6(nodes))

    