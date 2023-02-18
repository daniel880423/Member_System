def homework_9(bag_size, items): 
    # depth first search / breadth first search + backtracking
    values = [0 for i in range(bag_size + 1)]   #建立一個list
    for weight, price in items:                 #查找背包內容
        for i in range(bag_size, -1, -1):       #判斷題目要求是否成立，若成立則做加的動作
            if i + weight <= bag_size:
                if values[i + weight] < values[i] + price:
                    values[i + weight] = values[i] + price
    return max(values)

if __name__ == '__main__':
    bag_size = 1000
    items = [[100,1000],[100,1000],[100,1000]]
    print(homework_9(bag_size, items))
    # 335
    