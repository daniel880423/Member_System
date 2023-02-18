def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    global ans  
    ans = 0
    def DFS(size,price,ii,node):                                               #node是把所有跑過的節點放入，ii是為了不重複跑
        global ans
        if price > ans:
            ans = price
        for i in range(ii,len(items)):
            if i not in node and size <= bag_size:                             #如果i不在陣列裡，還有size小於等於背包size
                if (size + items[i][0]) > bag_size:                            #如果item的size加上原本的size大於背包承受的size，回for迴圈
                    continue
                DFS(size + items[i][0],price+items[i][1],i,node+[i])           #若滿足以上條件，把它加入背包
    DFS(0,0,0,[])
    return ans


if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    