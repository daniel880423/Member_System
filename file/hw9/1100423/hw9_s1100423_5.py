
def homework_9(bag_size, items):
#記錄當前最大收益
    max_value = 0
    def dfs(bag_size, items, value):
    # 如果物品清單為空，則更新 max_value 並退出遞迴
        if not items:
            nonlocal max_value
            max_value = max(max_value, value)
            return

        # 取出第一個物品
        item = items[0]
        weight = item[0]
        val = item[1]        

        # 當前背包容量不足以放入當前物品時，直接return
        if bag_size < weight:
            return dfs(bag_size, items[1:], value)

        # 當前搜索的收益小於當前最優解時 直接return
        if value + val <= max_value:                   ##value:背包目前收益  val:當前物品收益
            return dfs(bag_size, items[1:], value)

        # 該物品不放入背包，繼續遞迴搜索
        dfs(bag_size, items[1:], value)

        # 如果背包容量大於等於當前物品重量，則將該物品放入背包
        if bag_size >= weight:
            # 將該物品放入背包
            bag_size -= weight
            # 繼續遞迴搜索
            dfs(bag_size, items[1:], value + val)

    # 執行 DFS
    dfs(bag_size, items, 0)

    # 返回結果
    return max_value

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    #bag_size = 4
    #items = [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]]

    print(homework_9(bag_size, items))
    # 155
    