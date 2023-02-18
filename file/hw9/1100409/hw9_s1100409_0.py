def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking 
    def poi(wnow, pnow, items, bag_size):
        global mpnow

        tmww = wnow 
        tmpp = pnow
        
        if(items):   
            if wnow+items[0][0] <= bag_size: 
                wnow+=items[0][0] 

                pnow+=items[0][1] 
                poi(wnow, pnow, items[1:], bag_size) 

            else: 
                poi(wnow, pnow, items[1:], bag_size) 
            if pnow > mpnow:
                mpnow = pnow
            poi(tmww, tmpp, items[1:], bag_size)

    global mpnow 
    mpnow = 0
    wnow = 0 
    pnow = 0 #背包當前價值

    k = 0 #將items裡超過背包重量上限的物品忽略


    while k < len(items) :
        if items[k][0] > bag_size:
            del(items[k])
            k-=1
        k+=1

    poi(wnow, pnow, items, bag_size)
    return mpnow
    