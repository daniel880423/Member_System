def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    lenth=len(items)
    w=[]
    v=[]
    for i in items:
        w.append(i[0])
        v.append(i[1])
    dp=[[0 for i in range(bag_size+1)]for j in range(lenth)]

    for i in range (lenth):
        for j in range(bag_size+1):
            if j < w[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])

    for i in range(lenth):
        res = []
        for j in range(bag_size+1):
            res.append(dp[i][j])
    return res[-1]






    

if __name__ == '__main__':
    bag_size = 4
    items = [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]]
    print(homework_9(bag_size, items))
    # 155
    