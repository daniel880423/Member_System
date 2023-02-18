def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    def knapsack(volume, goods):
        dp = [[0] * (volume + 1) for _ in range(len(goods))]

        for j in range(1, volume + 1):  # 初始化
            if goods[0][0] <= j:  # 如果物品所佔空間(重量)小於容量j
                dp[0][j] = goods[0][1]  # 第一個物品的價值

        for i in range(1, len(goods)):
            for j in range(1, volume + 1):
                # 如果 物品i可以放下
                if goods[i][0] <= j:
                    # 當前物品價值 + 取當前物品後的剩餘空間
                    dp[i][j] = max(dp[i - 1][j], goods[i][1] + dp[i - 1][j - goods[i][0]])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp

    knapsack(bag_size, items)

    return max(max(knapsack(bag_size,items)))

if __name__ == '__main__':
    bag_size = 4
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    # 155
