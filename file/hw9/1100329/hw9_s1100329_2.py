def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    for a in items:                 #先處理資料中size本來就大於bag_size的情形
        if a[0]>bag_size:
            items.remove(a)
    queue=[[items[0][0],items[0][1],{0}]] #放置物品1並記錄走訪過的物品
    visit={(items[0][0],items[0][1])}   #存取物品，處理重複物品出現的情況
    total=[]                    #存取走訪過的組合
    maxprice=0                  #存取小偷的最高收益。
    q=0 
    while True:
        if len(queue)!=0:               ##判斷佇列是否為空
            bag=queue.pop(0)            #不為空就取出佇列第一個
            for i in range(len(items)):
                if i not in bag[2] and bag[0]+items[i][0]<=bag_size and (bag[2]|{i}) not in total:  #確定i不是已經納入的值 且 兩個size加起來不會超過bag_size 且 兩項聯集的組合不再total內
                    size=bag[0]+items[i][0]     #得到總和後的size   
                    price=bag[1]+items[i][1]    #得到總和後的price
                    if price>maxprice:          #確認price是否大於小偷的最高收益
                        maxprice=price
                    v=bag[2]|{i}                #取兩項的聯集放入V中
                    if size<bag_size:           #如果size本身就小於bag_size，在將增加佇列
                        queue.append([size,price,v])    
                    total.append(v)             ##記錄走過的組合
        if len(queue)==0 and q<len(items)-1:    #如果佇列長度為0，且q小於items的長度-1 進入
            q=q+1                               #q+1
            if (items[q][0],items[q][1]) in visit: #判斷是不是重複組合
                continue
            queue=[[items[q][0],items[q][1],{q}]]   #增加佇列
            visit.add((items[q][0],items[q][1]))    #記錄存取的物品
        if len(queue)==0:                       #如果佇列仍為0
            return maxprice                     #回傳最大收益

if __name__ == '__main__':
    bag_size = 1000
    items =  [[100,1000],[100,1000],[100,1000],[55,1005]]
    print(homework_9(bag_size, items))
    # 155



