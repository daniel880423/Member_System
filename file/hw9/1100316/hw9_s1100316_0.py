def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    global summ
    summ = 0
    i = len(items)
    dic = {}
    def DFS(size, price, visit,ll):
        global summ
        if price>summ:
            summ = price
        for a in range(ll,i):
            if a not in visit and size <= bag_size:
                if (size+items[a][0]>bag_size):
                    continue
                DFS(size+items[a][0],price+items[a][1],visit+[a],a)

    
    DFS(0,0,[],0)
    return summ

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    