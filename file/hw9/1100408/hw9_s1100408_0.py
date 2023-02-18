def homework_9(bag_size, items):
    # [depth first search] / breadth first search + backtracking
    N=len(items)
    Dic_visit={}                    #節點(價值,重量):profit
    for a in range(bag_size+1):
        Dic_visit[(0,a)]=0
    for i in range(1,N+1):
        for c in range(bag_size+1):
            if items[i-1][0]<=c:    #物品重量   #c背包耐重限制
                Dic_visit[(i,c)]=max(Dic_visit[i-1,c],items[i-1][1]+Dic_visit[(i-1,c-items[i-1][0])]) #max_price
            else:                     #物品不放進背包       #物品放進背包 背包價值上升   #耐重-背包重量        
                Dic_visit[(i,c)]=Dic_visit[(i-1,c)]     #size>bag_size，維持不變退回上一層


    return Dic_visit[(N,bag_size)]  # best value

if __name__ == '__main__':
    bag_size = 5
    items =  [[1,5],[3,1],[4,8],[6,100]]
    print(homework_9(bag_size, items))
    # 155
    