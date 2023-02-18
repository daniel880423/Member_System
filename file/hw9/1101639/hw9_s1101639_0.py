def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking 
    def promising(weight, price, items, bag_size):
        global maxtotalprice

        temweight = weight #複製一份未改變的weight price給不放入背包使用
        temprice = price
        
        if(items):   
            if weight+items[0][0] <= bag_size: #還可以偷
                weight+=items[0][0] #背包已有的重量加上此物的重量
                price+=items[0][1] #背包已有的價值加上此物的價值  
                promising(weight, price, items[1:], bag_size) #放入背包，下一項
            else: #偷不動這個
                promising(weight, price, items[1:], bag_size) #偷不動這個，下一項
            if price > maxtotalprice:
                maxtotalprice = price
            promising(temweight, temprice, items[1:], bag_size)#不放入背包，下一項

    global maxtotalprice #最大價值
    maxtotalprice = 0
    totalweight = 0 #背包當前重量
    totprice = 0 #背包當前價值

    i = 0 #將items裡超過背包重量上限的物品忽略
    while i < len(items) :
        if items[i][0] > bag_size:
            del(items[i])
            i-=1
        i+=1

    promising(totalweight, totprice, items, bag_size)
    return maxtotalprice
    