def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
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






    return 

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    