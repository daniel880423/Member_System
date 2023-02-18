def homework_9(bag_size, items):  # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    values = [0 for i in range(bag_size + 1)]
    for weight, price in items:
        for i in range(bag_size, -1, -1):
            if i + weight <= bag_size:
                if values[i + weight] < values[i] + price:
                    values[i + weight] = values[i] + price
    return max(values)

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    