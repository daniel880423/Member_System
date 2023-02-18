def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    n=len(items)
    global ans
    ans=[[-1 for i in range(bag_size + 1)] for j in range(n+1)]
    def dfs(items, W, n):                                                                    #定義深度優先搜尋函式
        if n==0 or W == 0:
            return 0
        if ans[n][W] != -1:
            return ans[n][W]
        
        if items[n-1][0] <= W:                                                               #放入的重量小於背包大小
            ans[n][W] = max(items[n-1][1]+dfs(items,W-items[n-1][0],n-1),dfs(items,W,n-1))   #跟除了自己外的東西比較
            return ans[n][W]
        elif items[n-1][0] > W:                                                              #放入重量超過背包大小
            ans[n][W] = dfs(items,W,n-1)                                                     #退回上一層
            return ans[n][W]
    
    dfs(items,bag_size,n)

    return ans[n][bag_size]

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    