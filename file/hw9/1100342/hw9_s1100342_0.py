def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    global profit,weight,maxprofit
    profit=0#累計獲益
    weight=0#累計重量
    maxprofit=0#當前最佳獲益
    def backtrack(n):
        global profit,weight,maxprofit
        if n >= len(items):
            #更新最佳獲益
            if maxprofit < profit:
                maxprofit = profit
        else:
            #重量小於背包容量，放入該珠寶
            if weight + items[n][0] <= bag_size:
                weight = weight + items[n][0]
                profit = profit + items[n][1]
                backtrack(n+1)
                #不放入該珠寶
                weight = weight - items[n][0]
                profit = profit - items[n][1]
            backtrack(n+1)                    

    backtrack(0)
    return maxprofit




if __name__ == '__main__':
    bag_size = 3
    items =  [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    