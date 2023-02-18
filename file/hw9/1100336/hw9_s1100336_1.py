def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    import copy
    copy_items=copy.deepcopy(items)    #先把超過bag_size的物品給刪掉
    for i in range(len(copy_items)):
        if copy_items[i][0]>bag_size:
            items.remove(copy_items[i])
    queue=[]
    for i, item in enumerate(items):
        queue.append(item + [{i}])
    #global max_price
    #visit=set()
    #visit.add(tuple(items[0]))
    max_price=items[0][1]
    total_visit=[]
    
    def bfs(queue,total_visit,max_price):
        while queue:
            size, price, v = queue.pop(0)
            if size <= bag_size:
                max_price = max(max_price,price)
            for i in range(len(items)):
                new_size=size+items[i][0]
                new_price=price+items[i][1]
                new_v = v | {i}
                if new_size<=bag_size and i not in v and new_v not in total_visit:#and price+items[i][1]>max_price  
                    # max_price=max(max_price,new_price)
                    queue.append([new_size,new_price,new_v])
                    total_visit.append(v)
                    #bfs(queue,items[i],total_visit,max_price)
        return max_price

    ans=bfs(queue,total_visit,max_price)

    
    return ans

if __name__ == '__main__':
    bag_size = 4
    items =  [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]]
#[[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    