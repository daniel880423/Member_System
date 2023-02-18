def homework_9(bag_size, items):
    # 定義全域變數 max_value 來記錄當前背包的最高收益
    global max_value
    max_value = 0
    
    def dfs(index, weight, value):
        # 如果當前物品已經超過物品總數，則退出遞迴
        if index >= len(items):
            return
        # 如果當前背包容量已經超過 bag_size，則退出遞迴
        if weight > bag_size:
            return
        # 更新 max_value 的值
        global max_value
        max_value = max(max_value, value)
        # 遞迴下一個物品，不加入該物品
        dfs(index + 1, weight, value)
        
        # 遞迴下一個物品，加入該物品
        dfs(index + 1, weight + items[index][0], value + items[index][1])
    
    # 從第一個物品開始遞迴
    dfs(0, 0, 0)
    
    return max_value


if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    #bag_size = 4
    #items = [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]]

    print(homework_9(bag_size, items))
    # 155
