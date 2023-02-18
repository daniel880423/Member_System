def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking

    lenth=len(items)
    w=[]
    v=[]
    for i in items:
        w.append(i[0])
        v.append(i[1])
    depth=[[0 for i in range(bag_size+1)]for j in range(lenth)] #初始深度

    for i in range (lenth):
        for j in range(bag_size+1):
            if j < w[i]:
                depth[i][j] = depth[i - 1][j]
            else:
                depth[i][j] = max(depth[i - 1][j], depth[i - 1][j - w[i]] + v[i])

    for i in range(lenth):
        result = []
        for j in range(bag_size+1):
            result.append(depth[i][j])
    return result[-1]






 

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    