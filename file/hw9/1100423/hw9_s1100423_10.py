def homework_9(bag_size, items):
    # 定義一個一維陣列 dp，其中 dp[j] 表示背包容量為 j 時的最大收益
    dp = [0] * (bag_size + 1)
    
    # 從前往後跑過每個物品
    for i in range(len(items)):
        weight = items[i][0]
        value = items[i][1]
        
        # 從後往前跑過每個背包容量
        for j in range(bag_size, weight - 1, -1):
            # 如果背包容量大於等於當前物品重量，則可以將該物品放入背包
            # 更新 dp[j]
            dp[j] = max(dp[j], dp[j - weight] + value)
    
    # 返回結果
    return dp[bag_size]


if __name__ == '__main__':
    bag_size = 12
    items = [[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    print(homework_9(bag_size, items))

if __name__ == '__main__':
    bag_size = 12
    items = [[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    print(homework_9(bag_size, items))