def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    # 定義一全局變量 max_value，記錄有限的背包容量下裝取多種珠寶的最高收益
    global max_value
    #將裝取多種珠寶的最高收益的背包初始化為0
    max_value = 0  

    def dfs(bag_size, items, value):
    # 如果物品清單無任何東西，則刷新 max_value 使其還原並退出遞迴
        if not items:
            global max_value
            max_value = max(max_value, value)
            return    
        # 取出第一個物品
        item = items[0]
        weight = item[0]
        val = item[1]
        # 將該物品不放入背包，繼續遞迴搜索
        dfs(bag_size, items[1:], value)
        # 如果背包容量大於或等於當前物品的重量，則可以將該物品放入背包
        if bag_size >= weight:
            # 將該物品放入背包
            bag_size -= weight
            # 繼續遞迴搜索
            dfs(bag_size, items[1:], value + val)
    # 進行深度優先搜尋
    dfs(bag_size, items, 0)

    # return結果
    return max_value

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    