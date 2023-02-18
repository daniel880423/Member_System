def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking 
    #用DFS法
    global ans                                                                 #用global定義ans，在homework_9和DFS內都能使用ans
    ans = 0
    def DFS(size,price,nodes,j):                                               #nodes紀錄所有走過的節點，j避免重複路徑({0,1}={1,0})
        global ans
        if price > ans:                                                        #若計算的price有增加，則改變ans值(max price)
            ans = price
        for i in range(j,len(items)):                                          #迴圈執行走訪節點
            if i not in nodes and size <= bag_size:                            #若節點沒有走過 & 背包放得下該物品大小
                if (size + items[i][0]) > bag_size:                            #若該物的size加上原本的size背包裝不下，則continue
                    continue                                                          
                DFS(size + items[i][0],price+items[i][1],nodes+[i],i)           #遞迴執行直到所有節點都走完
    DFS(0,0,[],0)
    return ans


if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    