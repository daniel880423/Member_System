def homework_9(bag_size,items):
    weight = []
    value = []
    n = 0
    for i in items:
        weight.append(i[0])
        value.append(i[1])
        n += 1
        # weight = [2, 4, 5, 6, 10, 3]
        # value = [1, 7, 4, 5, 11, 1]
    p = [[0 for j in range(bag_size + 1)] for i in range(n)]
    rec = [[0 for j in range(bag_size + 1)] for i in range(n)]
    for j in range(bag_size + 1):
            if weight[0] <= j:
                p[0][j] = value[0]
                rec[0][j] = 1
    for i in range(1, n):
            for j in range(bag_size + 1):
                if weight[i] <= j and value[i] + p[i-1][j-weight[i]] > p[i-1][j]:
                    p[i][j] = value[i] + p[i-1][j-weight[i]]
                    rec[i][j] = 1
                else:
                    p[i][j] = p[i-1][j]
    return (p[n-1][bag_size])
if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,20],[4,30],[1,130],[2,20]]
    #items = [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]]
    #bag_size = 4
    print(homework_9(bag_size,items))

    