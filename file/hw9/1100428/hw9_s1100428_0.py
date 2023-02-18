def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    def promising(totw, totp, items, bag_size):
        global maxtotp

        temw = totw 
        temp = totp
        
        if(items):   
            if totw+items[0][0] <= bag_size: 
                totw+=items[0][0] 
                totp+=items[0][1]
                promising(totw, totp, items[1:], bag_size) 
            else: 
                promising(totw, totp, items[1:], bag_size) 
            if totp > maxtotp:
                maxtotp = totp
            promising(temw, temp, items[1:], bag_size)

    global maxtotp 
    maxtotp = 0
    totw = 0 
    totp = 0 

    i = 0 
    while i < len(items) :
        if items[i][0] > bag_size:
            del(items[i])
            i-=1
        i+=1

    promising(totw, totp, items, bag_size)
    return maxtotp








if __name__ == '__main__':
    bag_size = 4
    items = [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]]

    print(homework_9(bag_size, items))
    # 320
    