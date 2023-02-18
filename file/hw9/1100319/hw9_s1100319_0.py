def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    total_visit = []
    visit = set()
    max_price = 0
    for i in range (len(items)):
        if items[i][0] > bag_size or tuple(items[i]) in visit:
            continue
        queue = [[items[i], {i}]]
        visit.add(tuple(items[i]))
        while queue:                        #如果queue裡還有東西
            currentVertex = queue.pop(0)    
            size = currentVertex[0][0]      #存取當前物品的size
            price = currentVertex[0][1]     #存取當前物品的price
            v = currentVertex[1]            #存取當前物品的v
            max_price = max(max_price,price) 
            if size == bag_size:            #如果當前物品的size等於背包限重
                continue                    #(代表無法加入其他物品)
            
            for i in range(len(items)):     #與除了自己以外的物品做比較    
                if i in v:                  #跳過同一個物品的比較
                    continue
                else:
                    new_size = items[i][0] + size   #存取既有物品加上新物品的size
                    new_price = items[i][1] + price #存取既有物品加上新物品的price
                    new_v = v | {i}                 #將新物品的位置加入v
                    #如果加入新物品的size不大於背包限重與new_v不在total_visit裡
                    if new_size <= bag_size and new_v not in total_visit: 
                        queue.append([[new_size,new_price],new_v])  #加到queue裡
                        total_visit.append(new_v)

    return max_price    


if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    