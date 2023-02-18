def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    def DFS(v,visit):
        global Max
        if len(visit)>0:
            t = visit[len(visit)-1] + 1
        else:
            t = 0
        for i in range(t,len(items)):
            n=(v[0]+items[i][0],v[1]+items[i][1])
            if  n[0]<=bag_size:
                Max=max(n[1],Max)
                DFS(n,visit+[i])

   
    global Max
    Max=0
    DFS((0,0),[])

    return Max

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    

