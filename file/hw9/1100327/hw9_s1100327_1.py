def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    
    def knapsack(n, size, val, total):#n是剩餘的物品個數 size是剩餘的背包空間 total用來儲存每種可行組合的最高價值
        if n == 0 or size == 0:#空間滿了或是全部放完就結束遞迴，迴傳答案
            total.append(val)
            return total
        if items[n-1][0] > size:#這個物品的size太大了，遞迴下一個
            knapsack(n-1, size, val, total)
        else:#背包還放得下該物品
            knapsack(n-1, size, val, total)#不選擇 繼續遞迴
            size-=items[n-1][0]
            val+=items[n-1][1]
            knapsack(n-1, size, val, total)#選擇這個物品，再遞迴下一層
    
    n = len(items)
    size = bag_size
    val = 0
    total = [0]
    knapsack(n, size, val, total)
    ans=max(total)
    
    return ans

if __name__ == '__main__':
    bag_size = 25
    items = [[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    print(homework_9(bag_size, items))
    # 155

           
