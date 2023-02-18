
def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    s = []
    p = []
    a = len(items)
    global maxx 
    maxx = 0
    for i in range(a):
        s.append(items[i][0])
        p.append(items[i][1])
    def DFS(size,price,visit):
        global maxx
        if size<=bag_size and price>maxx:
            maxx = price
        b = s[0:-1]
        for ii in visit:
            b[ii-1]=1001
        
        if size<=bag_size and price<maxx and bag_size-size>min(b):
            return None
        for i in range(a):
            if i not in visit and size <= bag_size:
                DFS(size + s[i],price+p[i],visit+[i])
    DFS(0,0,[])

    return maxx
if __name__ == '__main__':
    bag_size = 4
    items = [[2, 95], [3, 110], [4, 50], [1, 150], [2, 120], [1, 50]]
    print(homework_9(bag_size, items))
    # 155
    