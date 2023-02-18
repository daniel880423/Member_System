def homework_9(bag_size, items): 
    wt, val = zip(*items) #把重量和價值分成兩個tuple
    def dfs(i, j):
            if i < 0: 
                return 0
            ans = 0
            if j >= wt[i]: #如果還有空間放物品
                ans = max(ans, dfs(i-1, j-wt[i]) + val[i]) #更新
            ans = max(ans, dfs(i-1, j)) #比出最大收益
            return ans

    return dfs(len(val)-1, bag_size)

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))


    