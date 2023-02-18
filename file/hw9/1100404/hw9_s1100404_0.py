def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    NN = len(items)                                                                                           #將物品總數給到變數NN
    
    Dic_visit = {}                                                                                            #初始化陣列儲存節點(價值,重量):profit
    
    for a in range(bag_size + 1):
        
        Dic_visit[(0, a)]=0
    
    for i in range(1, NN + 1):                                                                                #一個一個物品檢查
        
        for c in range(bag_size + 1):                                                                         #c變數從最小到背包總重量限制
            
            if items[i - 1][0] <= c:                                                                          #如果第i(i-1是因為佇列是從0開始)個物品重量比c小，則可以放進背包
                
                Dic_visit[(i, c)] = max(Dic_visit[i - 1,c],items[i - 1][1] + Dic_visit[(i - 1,c - items[i - 1][0])])    #原先的物品總價值跟放進此物品的價值取價值高者輸入為當下Maxprofit
            
            else:                                                                                             #否則物品不放進背包
                
                Dic_visit[(i, c)] = Dic_visit[(i - 1, c)]                                                     #重量超過背包載重，維持不變退回上一層


    return Dic_visit[(NN, bag_size)]                                                                         # 回傳best value


if __name__ == '__main__':
    bag_size = 25
    items = [[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    print(homework_9(bag_size, items))
    # 155
    