def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking 
    def promising(total_weight, total_price, items, bag_size):
        global maxtotp

        temw = total_weight 
        temp = total_price
        
        if(items):   
            if total_weight+items[0][0] <= bag_size: 
                total_weight+=items[0][0] 
                total_price+=items[0][1] 
                promising(total_weight, total_price, items[1:], bag_size) 
            else: 
                promising(total_weight, total_price, items[1:], bag_size) 
            if total_price > maxtotp:
                maxtotp = total_price
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
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155