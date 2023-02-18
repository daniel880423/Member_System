def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    queue = []          #設定佇列
    total_visit = []    #設定total_visit
    total_index = set() #此set為存取所有item的index
    l = len(items)      #l = items長度

    for i in range(l): #將所有item加入queue，會有三個值[size,price,{visit}]
        v = items[i]     #v用來暫存，先將題目給的[size,price]給他
        v.append({i})  #再將{visit}加到v裡
        queue.append(v) #再將v存到queue裡
        total_index.add(i) #再將i2存到total_index裡

    #廣度優先
    max_price=0             #max_price預設為0
    while queue!=[]:        #當佇列不是空的
        #優化用
        total_visit = []    #當進到下一層判斷，total上一層的值就可以刪掉了，如進到第2層，第一層的visit{1},{2}...就不用了，因為第二層有兩個數字{1,2},{2,3}...
        for i3 in range(len(queue)):    #此行的i3用不到，功能是優化程式碼，與17行一起用
            #廣度優先
            size,price,visit = queue.pop(0) #將pop出來的item，三個值分別對應三個參數
            if size == bag_size:continue    #如果size = 最大重量，就continue
            for j in total_index-visit:     #j是total_index(所有index)跟visit(走過的index)差集的值
                if size+items[j][0]<=bag_size and visit | {j} not in total_visit: #如果size加下一個的重量還沒超過bag_size和visit加上下一個index不在total_visit中
                    new_node = [size+items[j][0],price+items[j][1],visit|{j}]     #new_node = pop出來的item加上新的item
                    queue.append(new_node)                                        #將new_node加到佇列中
                    if new_node[1]>max_price:                                     #如果new_node的價值>max_price
                        max_price = new_node[1]                                   #更新max_price為new_node的價值
                    total_visit.append(new_node[2])                               #total_visit加上new_node的visit
    return max_price                                                              #回傳max_price

if __name__ == '__main__':
    bag_size = 10000
    items = [[100, 1000], [100, 1000], [100, 1000], [100, 1000], [100, 1000], [100, 1000], [100, 1000], [100, 1000], [100, 1000], [100, 1000]]
    print(homework_9(bag_size, items))
    # 155
    