def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    N=len(items)
    Dic_visit={}                    #節點(價值,重量):profit
    for a in range(bag_size+1):
        Dic_visit[(0,a)]=0
    for i in range(1,N+1):
        for Weight in range(bag_size+1):
            if items[i-1][0]<=Weight:    #物品重量   #Weight背包耐重限制
                Dic_visit[(i,Weight)]=max(Dic_visit[i-1,Weight],items[i-1][1]+Dic_visit[(i-1,Weight-items[i-1][0])]) #max_price
            else:                     #物品不放進背包       #物品放進背包 背包價值上升   #耐重-背包重量        
                Dic_visit[(i,Weight)]=Dic_visit[(i-1,Weight)]     #size>bag_size，維持不變退回上一層


    return Dic_visit[(N,bag_size)]  # best value



if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    