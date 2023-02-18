def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    item_lenth = len(items)
    a = []
    b = []
    for i in items:
        a.append(i[0])
        b.append(i[1])
    s = [[0 for i in range(bag_size +1)] for j in range (item_lenth)]

    for i in range (item_lenth):
        for j in range (bag_size+1):
            if j < a[i]:
                s[i][j] = s[i - 1][j]
            else:
                s[i][j] = max(s[i - 1][j], s[i - 1][j - a[i]] + b[i])

    for i in range (item_lenth):
        ans = []
        for j in range(bag_size+1):
            ans.append(s[i][j])
    return ans[-1]






    

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    