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
    items = [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]]
    print(homework_9(bag_size, items))
    # 320
    