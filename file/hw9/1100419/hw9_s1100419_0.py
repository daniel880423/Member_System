def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking

    len_items=len(items)
    weight=[] #物品重量
    price=[] #物品價值
    for i in items:
        weight.append(i[0])
        price.append(i[1])
    matrix=[[0 for i in range(bag_size+1)]for j in range(len_items)]
    #設立一個初始為0空矩陣

    for i in range (len_items):
        for j in range(bag_size+1):
            if j < weight[i]:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - weight[i]] + price[i])
    #用迴圈找出最佳方法

    for i in range(len_items):
        re = []
        for j in range(bag_size+1):
            re.append(matrix[i][j]) #將找出的所有結果填入
    return re[-1]




if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    