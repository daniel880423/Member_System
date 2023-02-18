def homework_9(bag_size, items): 
    # depth first search / breadth first search + backtracking
    values = [0 for i in range(bag_size + 1)]
    for weight, price in items:
        for i in range(bag_size, -1, -1):
            if i + weight <= bag_size:
                if values[i + weight] < values[i] + price:
                    values[i + weight] = values[i] + price
    return max(values)

if __name__ == '__main__':
    bag_size = 5
    items = [[1,45],[2,100],[3,130],[1,80],[5,220],[5,200],[1,110]]
    print(homework_9(bag_size, items))
    # 235
    