def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking 
    
    global tot_p      
    tot_p = 0     #總收益
    b_w = 0      #背包重量
    b_p = 0      #背包價值
    
    
    def promising(b_w, b_p, items, bag_size):
        global tot_p

        w = b_w       #暫存背包重量和背包價值
        p = b_p
        
        if(items):   
            if b_w+items[0][0] <= bag_size:      #和背包空間比，若此物重量小於等於則裝入
                b_w+=items[0][0]     #背包原有重量加上此物的重量
                b_p+=items[0][1]     #背包原有價值加上此物的價值  
                promising(b_w, b_p, items[1:], bag_size)      #放入背包，下一項
            else: 
                promising(b_w, b_p, items[1:], bag_size)      #同上，大於則跳過，下個物品
            if b_p > tot_p:       #若新收益大於原收益
                tot_p = b_p       #則更新總收益
            promising(w, p, items[1:], bag_size)      #不放入背包，下一項

    

    m = 0 
    while m < len(items) :
        if items[m][0] > bag_size:      #若物品重量原本就超過背包重量上限的物品,則忽略
            del(items[m])
            m-=1
        m+=1

    promising(b_w, b_p, items, bag_size)
    return tot_p

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    