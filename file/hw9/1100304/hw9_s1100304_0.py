def homework_9(bag_size, items): 
    global max_price, size, price, visit
    def Backtrack(t):
        global max_price, size, price, visit

        if t > len(items):                      #DFS完成
            if max_price < price:
                max_price = price
        else:                                   #DFS未完成
            if size + lst[t][0] <= bag_size:    #第t個珠寶可以放到背包中
                size += lst[t][0]
                price += lst[t][1]
                Backtrack(t+1)
                size -= lst[t][0]
                price -= lst[t][1]
            if visit[t] + price > max_price:    #再搜尋下去
                Backtrack(t+1)

    lst = [[0,0]]                               #為了第36行，防止index超出範圍
    sumW = 0
    sumV = 0  
    for i in range(len(items)):
        sumW += items[i][0]                     #總重
        sumV += items[i][1]                     #總價值
        lst.append(items[i])                   

    max_price = 0
    size = 0
    price = 0

    visit = [0 for i in range(len(items)+1)]    #求剩下物品總價值
    visit[0] = sumV
    for i in range(1, len(items)+1):
        visit[i] = visit[i-1] - lst[i][1]

    if sumW > bag_size:                       
        Backtrack(1)
        return max_price
    else:                                       #總重 < 背包容量 ==> 全部帶走
        return sumV
              

if __name__ == '__main__':
    bag_size = 1000
    items = [[100,1000],[100,1000],[100,1000]]
    print(homework_9(bag_size, items))
    # 155

