def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    global weight, value, p, a
    a = items
    weight = []
    value = []
    p = [[None for j in range(bag_size+1)]for k in range(len(a))]
    for i in range(len(a)):
        weight.append(a[i][0])
        value.append(a[i][1])
    return backpack(len(a)-1, bag_size)


                
def backpack(i, size):
    if size < 0:
        return -float("inf")
    if i < 0:
        return 0
    if p[i][size]:
        return p[i][size]
    p[i][size] = max(backpack(i-1, size - weight[i]) + value[i], backpack(i-1, size))
    return p[i][size]

if __name__ == '__main__':
    bag_size = 5
    items = [[1, 5], [3, 1], [4, 8], [6, 100]]
    print(homework_9(bag_size, items))
    
    