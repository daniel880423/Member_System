def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    NN=len(items)
    Dic_visit={}
    for a in range(bag_size+1):
        Dic_visit[(0,a)]=0
    for i in range(1,NN+1):
        for c in range(bag_size+1):
            if items[i-1][0]<=c:
                Dic_visit[(i,c)]=max(Dic_visit[i-1,c],items[i-1][1]+Dic_visit[(i-1,c-items[i-1][0])])
            else:
                Dic_visit[(i,c)]=Dic_visit[(i-1,c)]


    return Dic_visit[(NN,bag_size)]


if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    