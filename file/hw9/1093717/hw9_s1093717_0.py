def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    def dfs(size,price,visit,max_price):
        if size <= bag_size:
            max_price = max(price,max_price)
        for i in range(len(items)):
            if size <= bag_size and i not in visit:
                max_price = max(max_price,dfs(size+items[i][0],price+items[i][1],visit+[i],max_price))
        return max_price

    return dfs(0,0,[],0)






if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    