def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking 
    def dfs(totw, totp, items, bag_size):                                    #一項物品，可選要放入背包或不放入背包(在節點時進行判斷)
        global maxp 

        temw = totw                                                          #複製一份未改變的totw totp給不放入背包使用
        temp = totp
        
        if(items):   
            if totw + items[0][0] <= bag_size:                               #背包尚有空間
                totw += items[0][0]                                          #背包已有的重量加上此物的重量
                totp += items[0][1]                                          #背包已有的價值加上此物的價值  
                dfs(totw, totp, items[1:], bag_size)                         #放入背包，下一項
            else:                                                            
                dfs(totw, totp, items[1:], bag_size)                         #背包沒空間，下一項
            if totp > maxp:                                                  #背包已有的價值加上此物的價值
                maxp = totp                                                  #變更可偷的最大價值
            dfs(temw, temp, items[1:], bag_size)                             #不放入背包，下一項
    global maxp                                                              #可偷的最大價值
    maxp = 0
    totw = 0                                                                 #當前背包總重量
    totp = 0                                                                 #當前背包總價值

    i = 0                                                                    #除去items裡超過背包重量上限的物品忽略
    while i < len(items) :
        if items[i][0] > bag_size:
            del(items[i])
            i-=1
        i+=1

    dfs(totw, totp, items, bag_size)
    return maxp                                                              #回傳可偷的最大價值

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    