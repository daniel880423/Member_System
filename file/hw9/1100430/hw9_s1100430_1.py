def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking 
    
    global total_profit      
    total_profit = 0     #總收益
    bag_weight = 0      #背包重量
    bag_profit = 0      #背包價值
    
    
    def promising(bag_weight, bag_profit, items, bag_size):
        global total_profit

        temw = bag_weight       #暫存背包重量和背包價值
        temp = bag_profit
        
        if(items):   
            if bag_weight+items[0][0] <= bag_size:      #和背包空間比，若此物重量小於等於則裝入
                bag_weight+=items[0][0]     #背包原有重量加上此物的重量
                bag_profit+=items[0][1]     #背包原有價值加上此物的價值  
                promising(bag_weight, bag_profit, items[1:], bag_size)      #放入背包，下一項
            else: 
                promising(bag_weight, bag_profit, items[1:], bag_size)      #同上，大於則跳過，下個物品
            if bag_profit > total_profit:       #若新收益大於原收益
                total_profit = bag_profit       #則更新總收益
            promising(temw, temp, items[1:], bag_size)      #不放入背包，下一項

    

    x = 0 
    while x < len(items) :
        if items[x][0] > bag_size:      #若物品重量原本就超過背包重量上限的物品,則忽略
            del(items[x])
            x-=1
        x+=1

    promising(bag_weight, bag_profit, items, bag_size)
    return total_profit

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    