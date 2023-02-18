def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    max_profit=0                                                    #紀錄最大利益
    queue=[]                                                   
    for j in  range (len(items)):
        queue.append(items[j])                                      #放置各個物品並將本物放入走訪過的物品中
        queue[-1].append({j})
    total_visit=[]                                                  #記錄走訪過的組合
    while  queue!=[]:                                               #廣度優先走訪
        total_visit = []
        for _ in range(len(queue)):
            weight,item_profit,visit_item=queue.pop(0)              #將重量、利益、走訪過的物品取出     
            for i in range (len(items)):    
                if visit_item|{i} in total_visit or i in visit_item:#若走訪物品的組合已出現過就直接跳過
                    continue                                        
                size=weight+items[i][0]                             #與各個物品重量相加
                if size>bag_size:                                   #若超出背包限制便跳過
                    continue
                profit=item_profit+items[i][1]                      #與各個物品的利益相加
                if profit>max_profit:                               #若出現新的利益最大值，將此次利益設定為新的利益最大值
                    max_profit=profit
                queue.append([size,profit,visit_item|{i}])          #將符合條件的物品加入走訪過的物品中
                total_visit.append(visit_item|{i})                  #將新走訪過的組合加入total_visit

    return max_profit



if __name__ == '__main__':
    bag_size = 4
    items =  [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]] 
    print(homework_9(bag_size, items))
    # 155

    