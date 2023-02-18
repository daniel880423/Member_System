

def homework_9(bag_size, items):
    # 定義一個二維陣列 memo，其中 memo[i][j] 表示前 i 個物品，且背包容量為 j 時的最大收益
    memo = [[-1] * (bag_size + 1) for _ in range(len(items) + 1)]
    
    def dfs(bag_size, items, i, memo, max_profit):
        # 如果已經搜索到了最後一個物品，則返回結果
        if i == len(items):
            return 0
        
        # 如果已經記錄過該子問題的結果，則直接返回
        if memo[i][bag_size] != -1:
            return memo[i][bag_size]
        
        # 當前背包容量不足以放入當前物品時，直接return
        if bag_size < items[i][0]:
            return dfs(bag_size, items, i + 1, memo, max_profit)
        
        # 不放入背包
        res = dfs(bag_size, items, i + 1, memo, max_profit)
        
        # 放入背包
        profit = dfs(bag_size - items[i][0], items, i + 1, memo, max_profit) + items[i][1]
        
        # 當前搜索分支的收益大於當前最優解 更新max
        if profit > max_profit:
            res = max(res, profit)
            max_profit = profit
        
        #記錄子問題的結果
        memo[i][bag_size] = res
        
        # 返回結果
        return res
    
    return dfs(bag_size, items, 0, memo, 0)
if __name__ == '__main__':
    bag_size = 12
    items = [[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    #bag_size = 4
    #items = [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]]

    print(homework_9(bag_size, items))
    # 155
    