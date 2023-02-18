def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking 
    def promising(totw, totp, items, bag_size):
        global maxtotp

        temw = totw #複製一份未改變的totw totp給不放入背包使用
        temp = totp
        
        if(items):   
            if totw+items[0][0] <= bag_size: #還可以偷
                totw+=items[0][0] #背包已有的重量加上此物的重量
                totp+=items[0][1] #背包已有的價值加上此物的價值  
                promising(totw, totp, items[1:], bag_size) #放入背包，下一項
            else: #偷不動這個
                promising(totw, totp, items[1:], bag_size) #偷不動這個，下一項
            if totp > maxtotp:
                maxtotp = totp
            promising(temw, temp, items[1:], bag_size)#不放入背包，下一項

    global maxtotp #最大價值
    maxtotp = 0
    totw = 0 #背包當前重量
    totp = 0 #背包當前價值

    i = 0 #將items裡超過背包重量上限的物品忽略
    while i < len(items) :
        if items[i][0] > bag_size:
            del(items[i])
            i-=1
        i+=1

    promising(totw, totp, items, bag_size)
    return (maxtotp)

if __name__ == '__main__':
    bag_size = 4
    items = [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]] #[1,150],[2,120],[1,50]
    print(homework_9(bag_size, items))
    # 155
    