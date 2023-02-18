def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking

    global maxtotp

        abag = bagx     #設bagy為未改變的totp， copy原本的totp給不放入背包使用
        bbag = bagy
        
        if(items):   
            if  bagx + items[0][0] <= bag_size: 
                bagx += items[0][0] 
                bagy += items[0][1]   
                promising(bagx, bagy, items[1:], bag_size) 
            else:
                promising(bagx, bagy, items[1:], bag_size) 
            if bagy > maxtotp:
                maxtotp = bagy
            promising(abag, bbag, items[1:], bag_size)

    global maxtotp 
    maxtotp = 0
    bagx = 0 
    bagy = 0 

    i = 0 
    while i < len(items) :
        if items[i][0] > bag_size:
            del(items[i])
            i-=1
        i+=1

    promising(bagx, bagy, items, bag_size)
    return maxtotp







    return 

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    