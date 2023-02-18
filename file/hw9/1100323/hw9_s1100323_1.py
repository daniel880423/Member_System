def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking 
    def abc(bagx, bagy, items, bag_size):
        global maxbag

        abag = bagx 
        bbag = bagy
        
        if(items):   
            if bagx+items[0][0] <= bag_size: 
                bagx+=items[0][0] 
                bagy+=items[0][1] 
                abc(bagx, bagy, items[1:], bag_size) 
            else: 
                abc(bagx, bagy, items[1:], bag_size) 
            if bagy > maxbag:
                maxbag = bagy
            abc(abag, bbag, items[1:], bag_size)

    global maxbag 
    maxbag = 0
    bagx = 0 
    bagy = 0 

    i = 0 
    while i < len(items) :
        if items[i][0] > bag_size:
            del(items[i])
            i-=1
        i+=1

    abc(bagx, bagy, items, bag_size)
    return maxbag