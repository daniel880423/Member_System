def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    l=len(items)
    a=[]
    b=[]
    for i in items:
        a.append(i[0])
        b.append(i[1])
    dep_first=[[0 for i in range(bag_size+1)]for j in range(l)]

    for i in range (l):
        for j in range(bag_size+1):
            if j < a[i]:
                dep_first[i][j] = dep_first[i - 1][j]
            else:
                dep_first[i][j] = max(dep_first[i - 1][j], dep_first[i - 1][j - a[i]] + b[i])

    for i in range(l):
        answer = []
        for j in range(bag_size+1):
            answer.append(dep_first[i][j])
    return answer[-1]




    return 

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    