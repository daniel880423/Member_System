def homework_9(bag_size, items):
    

    def promising(totw, totp, items, bag_size):
        global maxtop

        temppalc = totw                                                 #copy totw totp
        temcover = totp
        
        if     (items):   


            if totw + items[0][0] <= bag_size:                            #still bag

                totw += items[0][0]                                       #背包重+目標重量
                totp += items[0][1]                                       #背包val + goal.val  
                promising(totw, totp, items[1:], bag_size)                #放入 

            else: #偷不動這個

                promising(totw, totp, items[1:], bag_size)                #no pass and next

            if totp > maxtotp:

                maxtotp = totp
            promising(temppalc, temcover, items[1:], bag_size)            #no putin


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
    return maxtotp
    