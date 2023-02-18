def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    global wei_lst, pri_lst, number, Bag_size, max_price
    wei_lst = []
    pri_lst = []
    max_price = 0
    Bag_size = bag_size
    for i in range(len(items)):
        if items[i][0] > bag_size:      #如果物品本身size超過背包最大容量就不要加進wei_lst跟pri_lst中
            continue
        wei_lst.append(items[i][0])     #先將個物品重量跟價值分別放在wei_lst及pri_lst中
        pri_lst.append(items[i][1])
    number = len(wei_lst)
    dfs(index=0, size=0, price=0) #初值index、總size、總價值都先設0
    return max_price

def dfs(index, size, price):
    global max_price
    if index == number:         #從後面開始遞迴，遇到不超過bag_size且max_price大於目前儲存的數值，就更新max_price
        if size <= Bag_size and price > max_price:
            max_price = price
        return
    dfs(index + 1, size, price) # 不選擇物品
    dfs(index + 1, size + wei_lst[index], price + pri_lst[index]) # 選擇物品


if __name__ == '__main__':
    bag_size = 5
    items =  [[1,5],[3,1],[4,8],[6,100]]
    print(homework_9(bag_size, items))
    # 155