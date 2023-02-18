def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    mount=len(items)
    visit={}                                                                                        #節點(價值,重量)
    for a in range(bag_size+1):
        visit[(0,a)]=0
    for i in range(1,mount+1):
        for c in range(bag_size+1):
            if items[i-1][0]<=c:      #當物品重量比包包乘載量低時
                visit[(i,c)]=max(visit[i-1,c],items[i-1][1]+visit[(i-1,c-items[i-1][0])])   #測出最大價值(物品放進包包後比較)
            else:                             
                visit[(i,c)]=visit[(i-1,c)]                                                     #當size>包包size時，維持不變退回上一層


    return visit[(mount,bag_size)]



if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    