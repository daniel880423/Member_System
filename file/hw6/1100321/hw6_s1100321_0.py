from math import dist

def homework_6(nodes):

    ans=0                                                                                  #設定初始值
    b=0                                                                                    #設定初始值
    distance=[0,0,0,0]                                                                     #設定初始值

    for i in range(len(nodes)-1):                                                          #i從0到-2
        a= min(distance)                                                                   #找出對其他點的最小距離

        if i > 1:                                                                          #只有在i大於1的時候b才不會是0
                if a>b:                                                                    #如果對於Vx,Vx+1不是最小距離那就是b
                    distance=[b]

        ans+=min(distance)                                                                 #加起來
        distance.remove(min(distance))                                                     #將已經連到過的點去

        if len(distance)>=2:                                                               #如果沒有大於2會掛掉
            b = min(distance)

        del distance[0:4]                                                                  #刪掉前面

        for j in range(i+1,len(nodes)):                                                    #從(i+1,到最後)
            distance+=[abs((nodes[j][0]-nodes[i][0]))+abs((nodes[j][1]-nodes[i][1]))]      #計算距離
            if i == (len(nodes)-2):                                                        #如果剩兩個點直接相加
                ans+= min(distance)



    return ans

if __name__ == '__main__':
    nodes = [[3,1],[2,7],[4,8],[7,4]]
    print(homework_6(nodes))
    # 22
    