def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    maxprofit = 0   #最大增益
    profit = 0      #當下增益
    weight = 0      #背包重量
    value = []      #存入所有符合13行的profit值
    i = 0  
    knapsack(i,profit,weight,maxprofit,value,bag_size,items) 

    return max(value)
def knapsack(i,profit,weight,maxprofit,value,bag_size,items): #BFS + backtracking 函數
    if weight <= bag_size and profit > maxprofit:
            maxprofit = profit
            value.append(maxprofit)
    if promising(i,profit,weight,maxprofit,bag_size,items):
        knapsack(i+1,profit+items[i][1],weight+items[i][0],maxprofit,value,bag_size,items) #選擇要拿物品跑此函數
        knapsack(i+1,profit,weight,maxprofit,value,bag_size,items) #選擇不拿跑此函數

def promising(i,profit,weight,maxprofit,bag_size,items): #判斷有沒有promising
    if weight > bag_size:
        return False
    else:
        j = i
        bound = profit
        totweight = weight
        while j<len(items) and totweight+items[j][0]< bag_size:
            totweight = totweight+items[j][0]
            bound =bound+items[j][1]
            j+=1
        k = j
        if k<len(items):
            bound = bound + (bag_size-totweight)*(items[k][1]/items[k][0])
        return bound > maxprofit
if __name__ == '__main__':
    #bag_size = 3
    #items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    bag_size = 25
    items = [[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    print(homework_9(bag_size, items))
    # 155
    