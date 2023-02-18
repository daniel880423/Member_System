def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking

    
    global maxprice
    maxprice=0

    def dfs(size,price,visit):
        global maxprice 
        now = visit[-1]
        next=now+1
        if size+items[now][0]>bag_size:
            visit.pop()
            if next<len(items):
                visit.append(next)
                dfs(size, price, visit)
        else:
            size+=items[now][0]
            price+=items[now][1]
            if price>maxprice:
                maxprice=price
            if next<len(items):
                visit.append(next)
                dfs(size, price, visit)
            





    for i in items:
        if i[0]<=bag_size:
            dfs(0, 0, [items.index(i)])
    return maxprice

if __name__ == '__main__':
    bag_size = 25
    items = [[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    print(items[-1])
    print(homework_9(bag_size, items))
    # 155
    