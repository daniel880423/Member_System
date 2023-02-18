import queue
def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    dp = [[0]*(bag_size+1) for i in range(len(items))]
    for j in range(1,bag_size+1):#初始化
        if items[0][0] <= j:    #如果物品所占空間小於容量j
            dp[0][j] = items[0][1] #第一个物品的价值

    for i in range(1,len(items)):
        for j in range(1,bag_size+1):    # 如果物品i可以放下
            if items[i][0] <= j:    #物品价值 + 取物品后所剩空間
                dp[i][j] = max(dp[i-1][j],items[i][1]+dp[i-1][j-items[i][0]])
            else:
                dp[i][j] = dp[i-1][j]
        
    return dp[-1][-1]

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    