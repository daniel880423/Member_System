def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    len_item=len(items)
    weight=[]
    value=[]
    for i in items:
        weight.append(i[0])
        value.append(i[1])
    initial=[[0 for i in range(bag_size+1)]for j in range(len_item)]

    for i in range (len_item):
        for j in range(bag_size+1):
            if j < weight[i]:
                initial[i][j] = initial[i - 1][j]
            else:
                initial[i][j] = max(initial[i - 1][j], initial[i - 1][j - weight[i]] + value[i])

    for i in range(len_item):
        con = []
        for j in range(bag_size+1):
            con.append(initial[i][j])
    return con[-1]



if __name__ == '__main__':
    bag_size = 5
    items =  [[1,5],[3,1],[4,8],[6,100]]
    print(homework_9(bag_size, items))
    # 155
    
    