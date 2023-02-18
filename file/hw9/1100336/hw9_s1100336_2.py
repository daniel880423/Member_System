def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking

    #先把超過bag_size的物品給刪掉
    import copy
    copy_items=copy.deepcopy(items)    
    for i in range(len(copy_items)):
        if copy_items[i][0]>bag_size:
            items.remove(copy_items[i])

    queue=[]
    for i, item in enumerate(items):  #把items內每個item依照[size,price,{第幾個物品}]加入queue
        queue.append(item + [{i}])

    max_price=items[0][1]  #先把max_price預設為第一個items的價值
    total_visit=[]         
    
    def bfs(queue,total_visit,max_price): 
        while queue:                      #如果queue不是空的的話
            size, price, v = queue.pop(0)  #把queue內的第一個list([size,price,{第幾個物品}])，pop出來(有三個東西)依序存入size,price,和v這三個變數
            if size <= bag_size:           #如果這個pop出來的東西的size沒超過bag_size
                max_price = max(max_price,price)    #把新的price和之前的max_price比較，把叫大值存入max_price
            for i in range(len(items)):             
                new_size=size+items[i][0]           #設一變數new_size存queue的第一個size(items[i][0])和之前pop出去的size的和
                new_price=price+items[i][1]         #設一變數new_price存queue的第一個price(items[i][1])和之前pop出去的price的和
                new_v = v | {i}                     #設一變數new_v存queue的第一個v({i})和之前pop出去的v的聯集
                if new_size<=bag_size and i not in v and new_v not in total_visit:  #如果new_size沒大於bag_size，且這個物品還沒加入v，且new_v還沒加入total_visit
                    queue.append([new_size,new_price,new_v])    #就把這三個值以List的方式包在一起加進queue
                    total_visit.append(v)                       #再將v這個set加入total_visit

        return max_price

    ans=bfs(queue,total_visit,max_price)

    
    return ans

if __name__ == '__main__':
    bag_size = 4
    items =  [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]]
#[[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    