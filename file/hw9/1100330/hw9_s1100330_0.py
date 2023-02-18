def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    size = []                          
    value = []
    for i in items:
        if i[0] <= bag_size:
            size.append(i[0])
            value.append(i[1])

    s = len(size)

    x = []
    for i in range(s):
        x.append([0])
        for o in range(bag_size):
            x[i].append(0)

    for i in range(0,s):
        for j in range(bag_size,0,-1):
            if j<size[i]:
                x[i][j] = x[i-1][j]
            else:
                x[i][j] = max(x[i-1][j],x[i-1][j-size[i]]+value[i])
    
    return x[-1][-1]

if __name__ == '__main__':
    bag_size = 4
    items =  [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]]
    print(homework_9(bag_size, items))
    # 155
    